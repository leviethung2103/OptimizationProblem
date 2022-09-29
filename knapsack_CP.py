from ortools.sat.python import cp_model

capacities = 850
no_bin = 1



data = {}
data['values'] = [
    360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    312
]

no_items = len(data['values'])

data['weights'] = [
    7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
]

model = cp_model.CpModel()

## Create the variables
# if item i is packed in bin b, index: x[i,b]
x = {}
for i in range(no_items):
    x[i] = model.NewBoolVar(f'x_{i}')


## Create the constraints
# Each item is  assigned to at most one bin , sum <= 1 Khong can thiet



# The amount packed in each bin cannot exceed its capacity.
amount_packed = []
for i in range(no_items):
    amount_packed.append(x[i] * data['weights'][i])

model.Add(sum(amount_packed) <= capacities)


# Create the objective function 
objective = []
for i in range(no_items):
    objective.append(x[i] * data['values'][i]) 
    
model.Maximize(cp_model.LinearExpr.Sum(objective))

solver = cp_model.CpSolver()
status = solver.Solve(model)


if status == cp_model.OPTIMAL:
    print(f'Total packed value: {solver.ObjectiveValue()}')
    packed_items = []
    packed_weights = [] 
    for i in range(no_items):
        if solver.Value(x[i]) ==  1:
            packed_items.append(i)
            packed_weights.append(data['weights'][i])
    print('Packed items:', packed_items)
    print (f"Total packed weight: {sum(packed_weights)}")
    
else:
    print('The problem does not have an optimal solution.')