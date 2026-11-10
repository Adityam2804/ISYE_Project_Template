"""truck.py: Ellis's truck, as on the slides. Run: python truck.py (needs pulp below 4.0, which includes CBC)."""
from pulp import *

loads = {"Hygiene Kits": (100, 30), "Blankets": (250, 40), "Medical Kits": (250, 50),
         "Food Packs": (450, 60), "Water": (500, 70)}   # kg, points

model = LpProblem("truck", LpMaximize)
take = {n: LpVariable(n, cat="Binary") for n in loads}
model += lpSum(loads[n][1] * take[n] for n in loads)           # the objective
model += lpSum(loads[n][0] * take[n] for n in loads) <= 1000   # the constraint

# A second limit, volume: delete the # at the start of the next three lines
# volume = {"Hygiene Kits": 1, "Blankets": 6, "Medical Kits": 2,
#           "Food Packs": 3, "Water": 4}
# model += lpSum(volume[n] * take[n] for n in loads) <= 10

# A third constraint, the need for shelter or food: delete the # on the next line
# model += take["Blankets"] + take["Food Packs"] >= 1

model.solve(PULP_CBC_CMD(msg=0))
chosen = [n for n in loads if take[n].value() == 1]
print(LpStatus[model.status], chosen, value(model.objective))
