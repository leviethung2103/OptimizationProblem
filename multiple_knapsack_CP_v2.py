from ortools.sat.python import cp_model

capacities = [100,100,100,100,100]
no_bin = 5 

data = {}
data['weights'] = [
    48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36
]
data['values'] = [
    10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25
]
no_items = len(data['values'])
model = cp_model.CpModel()

## Create the variables
# if item i is packed in bin b, index: x[i,b]
x = {}
for i in range(no_items):
    for b in range(no_bin):
        x[i,b] = model.NewBoolVar(f'x_{i}_{b}')


## Create the constraints
# Each item is  assigned to at most one bin , sum <= 1 Khong can thiet
# C1
# for i in range(no_items):
#     assign_item = []
#     for b in range(no_bin):
#         assign_item.append(x[i,b])
#     model.Add(sum(assign_item) <= 1)
# Another C1
for i in range(no_items):
    model.Add(sum(x[i,b] for b in range(no_bin)) <= 1)

# The amount packed in each bin cannot exceed its capacity.
# C2
# for b in range(no_bin):
#     amount_packed = []
#     for i in range(no_items):
#         amount_packed.append(x[i,b] * data['weights'][i])
#     model.Add(sum(amount_packed) <= capacities[b])

# Another C2
for b in range(no_bin):
    model.Add(sum(x[i,b] * data['weights'][i] for i in range(no_items)) <= capacities[b])

# Create the objective function 
objective = []
# C3
for i in range(no_items):
    for b in range(no_bin):
        objective.append(x[i,b] * data['values'][i]) 
        
print (objective)

model.Maximize(cp_model.LinearExpr.Sum(objective))

solver = cp_model.CpSolver()
status = solver.Solve(model)


if status == cp_model.OPTIMAL:
    print(f'Total packed value: {solver.ObjectiveValue()}')
    total_weight = 0
    for b in range(no_bin):
        print(f'Bin {b}')
        bin_weight = 0
        bin_value = 0
        for i in range(no_items):
            if solver.Value(x[i, b]) > 0:
                print(
                    f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                )
                bin_weight += data['weights'][i]
                bin_value += data['values'][i]
        print(f'Packed bin weight: {bin_weight}')
        print(f'Packed bin value: {bin_value}\n')
        total_weight += bin_weight
    print(f'Total packed weight: {total_weight}')
else:
    print('The problem does not have an optimal solution.')