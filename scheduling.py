from ortools.sat.python import cp_model

num_nurses = 4 
num_days = 3 
num_shifts = 3 

# variables
# nurse_i will work on date d
shifts = {}
for i in range(num_nurses):
    for d in range(num_days):
        for s in range(num_shifts):
            shifts[i,d,s] = model.NewBoolVar(f'shift_{i}_{d}_{s}')


# Each shift is assigned to a single nurse per day.
# Each nurse works at most one shift per day.
for d in range(num_days):
    for s in range(num_shifts):
        model.AddExactlyOne(shifts[i,d,s] for i in range(num_nurses)) 

# Next, here's the code that requires that each nurse works at most one shift per day.
for i in range(num_nurses):
    for d in range(num_days):
        model.AddAtMostOne(shifts[i,d,s] for s in range(num_shifts))
        
        
# Next, we show how to assign shifts to nurses as evenly as possible. 
# Since there are nine shifts over the three-day period, we can assign two shifts to each of the four nurses. 
# After that there will be one shift left over, which can be assigned to any nurse.

# The following code ensures that each nurse works at least two shifts in the three-day period.
# min_shifts_per_nurse = 2 , each nurse works 2 
# distribute the shift evenly.
# Total of shifts = 9 for 3 days is not divisible by the number of nurses = 4. some nurses will be assigned one more shift 
# 1 nurse may be work 2 shifts, 1 nurse may be work 3 shift
# 4*2 + 1 =9 

min_shifts_per_nurse = (num_shifts * num_days) // num_nurses

# calculate the max_shifts > 1 nurse amy be work 3 shifts
if num_shifts * num_days % num_nurses == 0:
    max_shifts_per_nurse = min_shifts_per_nurse
else:
    max_shifts_per_nurse = min_shifts_per_nurse + 1 

# constraints abou the min shift and max shift per nurse
for i in range(num_nurses):
    num_shift_worked = []
    for d in range(num_days):
        for s in range(num_shifts):
            num_shift_worked.append(shifts[i,d,s])
    model.Add(min_shifts_per_nurse <= sum(num_shift_worked))
    model.Add(max_shifts_per_nurse >= sum(num_shift_worked))


solver.parameters.linearization_level = 0
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True


class NursesPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, shifts, num_nurses, num_days, num_shifts, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._shifts = shifts
        self._num_nurses = num_nurses
        self._num_days = num_days
        self._num_shifts = num_shifts
        self._solution_count = 0
        self._solution_limit = limit

    def on_solution_callback(self):
        self._solution_count += 1
        print('Solution %i' % self._solution_count)
        for d in range(self._num_days):
            print('Day %i' % d)
            for n in range(self._num_nurses):
                is_working = False
                for s in range(self._num_shifts):
                    if self.Value(self._shifts[(n, d, s)]):
                        is_working = True
                        print('  Nurse %i works shift %i' % (n, s))
                if not is_working:
                    print('  Nurse {} does not work'.format(n))
        if self._solution_count >= self._solution_limit:
            print('Stop search after %i solutions' % self._solution_limit)
            self.StopSearch()

    def solution_count(self):
        return self._solution_count

# Display the first five solutions.
solution_limit = 5
solution_printer = NursesPartialSolutionPrinter(shifts, num_nurses,
                                                num_days, num_shifts,
                                                solution_limit)

solver.Solve(model, solution_printer)