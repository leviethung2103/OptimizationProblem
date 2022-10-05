from ortools.sat.python import cp_model

# Decalre hte model
model = cp_model.CpModel()

# Create the variables
x = model.NewIntVar(0, 50, 'x')
y = model.NewIntVar(0,50,'y')


# Define the constraints
# has non-integer coefficients, you must first multiply the entire constraint by a sufficiently large integer 
# to convert the coefficients to integers. In this case, you can multiply by 2, which results in the new constraint
model.Add(2*x+14*y <= 35)
model.Add(2*x <= 7)
model.Add(x >= 0)
model.Add(y >= 0)

# Define the objective function
model.Maximize(x+10*y)

# Call the solver
solver = cp_model.CpSolver()
status = solver.Solve(model)


# Display the solution
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'Maximum of objective function: {solver.ObjectiveValue()}\n')
    print(f'x = {solver.Value(x)}')
    print(f'y = {solver.Value(y)}')
else:
    print('No solution found.')