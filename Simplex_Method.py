# The problem is described at here: https://www.youtube.com/watch?v=vVzjXpwW2xI 
from ortools.sat.python import cp_model

num_nurses = 4 
num_days = 3 
num_shifts = 3 


# variables 
# x1: type A
# x2: type B 
# x3: type C
model = cp_model.CpModel()
    
x1 = model.NewIntVar(0,1000,'x1')
x2= model.NewIntVar(0,1000,'x2')
x3= model.NewIntVar(0,1000,'x3')

# constraints 
model.Add(2*x1 + 3*x2 + 2*x3 <= 1000)
model.Add(1*x1 + 1*x2 + 2*x3 <= 800)

# Maximize the profit 
model.Maximize(7*x1 + 8*x2 + 10*x3)

# Call the solver
solver = cp_model.CpSolver()
status = solver.Solve(model)


# Display the solution
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'Maximum of objective function: {solver.ObjectiveValue()}\n')
    print(f'x1 = {solver.Value(x1)}')
    print(f'x2 = {solver.Value(x2)}')
    print(f'x3 = {solver.Value(x3)}')
else:
    print('No solution found.')