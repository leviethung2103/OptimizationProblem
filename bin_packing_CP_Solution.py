from ortools.sat.python import cp_model


model = cp_model.CpModel()
data = {
    "weights":  [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30],
    "values" : []
}
# num_items
data['all_items'] = range(len(data['weights']))
# num of bins = number of items
data['all_bins'] = data['all_items']
# maximum capacity for 1 bin
data['bin_capacity'] = 100
    
# Define the variables
# x[i, b] = 1 if item i is packed in bin b.
x = {}
for i in data['all_items']:
    for b in data['all_bins']:
        x[i, b] = model.NewBoolVar(f'x_{i}_{b}')

# y[j] = 1 if bin j is used
y = {}
for i in data['all_bins']:
    y[i] = model.NewBoolVar(f'y_{i}')
    
        
# Each item is assigned to exactly one bin.
for i in data['all_items']:
    model.AddExactlyOne(x[i, b] for b in data['all_bins'])


# The amount packed in each bin cannot exceed its capacity.
for b in data['all_bins']:
    model.Add(
        sum(x[i, b] * data['weights'][i]
            for i in data['all_items']) <= data['bin_capacity']*y[b])
    
    
# Minimize the number of bins 
objective = []
for b in data['all_bins']:
    objective.append(y[b])

model.Minimize(cp_model.LinearExpr.Sum(objective))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print ("Found the solution")
    num_bins = 0
    # total_weight = 0
    for b in data['all_bins']:
        if solver.Value(y[b]) == 1:
            bin_items = []
            bin_weight = 0
            for i in data['all_items']:
                if solver.Value(x[i,b]) > 0:
                    bin_items.append(i)
                    bin_weight += data['weights'][i]
            if bin_weight > 0:
                num_bins += 1
                print (f"Bin number {b}")
                print (f"   Item packed: ", bin_items)
                print (f"   Total weight: ", bin_weight)
    print('Number of bins used:', num_bins)
else:
    print('The problem does not have an optimal solution.')
