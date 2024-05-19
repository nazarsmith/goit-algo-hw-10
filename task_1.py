import pulp


model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)
L = pulp.LpVariable('L', lowBound=0, upBound=50, cat='Integer')  # lemonade
J = pulp.LpVariable('J', lowBound=0, upBound=20, cat='Integer')  # juice


model += L + J, "Profit"



model +=  2 * L + J <= 100 # water constraint
model += L <= 50 # sugar contraint
model += L <= 30 # lemon juice constraint
model += 2 * J <= 40 # puree constraint

model.solve()

print("Produce units of lemonade:", L.varValue)
print("Produce units of juice:", J.varValue)
