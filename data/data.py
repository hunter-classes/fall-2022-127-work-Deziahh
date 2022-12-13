import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import csv

reader = csv.DictReader(open("cereal.csv"))
data = [x for x in reader]

def findPercentage(num1, total):
    return (num1 / total) * 100

manufact = [x["mfr"] for x in data]

aCount = 0
for item in manufact:
    if "A" in item:
        aCount += 1
        
gCount = 0
for item in manufact:
    if "G" in item:
        gCount += 1
        
kCount = 0
for item in manufact:
    if "K" in item:
        kCount += 1

nCount = 0
for item in manufact:
    if "N" in item:
        nCount += 1

pCount = 0
for item in manufact:
    if "P" in item:
        pCount += 1
        
qCount = 0
for item in manufact:
    if "Q" in item:
        qCount += 1

rCount = 0
for item in manufact:
    if "R" in item:
        rCount += 1

print(aCount, "of the cereals are manufactured by American Home Food Products.")
print(gCount, "of the cereals are manufactured by General Mills.")
print(kCount, "of the cereals are manufactured by Kelloggs.")
print(nCount, "of the cereals are manufactured by Nabisco.")
print(pCount, "of the cereals are manufactured by Post.")
print(qCount, "of the cereals are manufactured by Quaker Oats.")
print(rCount, "of the cereals are manufactured by Ralston Purina.")

type = [x["type"] for x in data]
hType = 0
for item in type:
    if "H" in item:
        hType += 1

cType = 0
for item in type:
    if "C" in item:
        cType += 1

total = len(type)
result = findPercentage(hType, total)
print(result, "percent of the cereal is hot.")

#graph data:

fig, ax = plt.subplots(figsize=(10,3), layout='constrained')
categories = ['AHFP', 'General Mills', 'Kelloggs', 'Nabisco', 'Post', 'Quaker Oats', 'Ralston Purina']
counts = [1, 22, 23, 6, 9, 8, 8]

ax.bar(categories, counts);

ax.set_ylim(0, 25)

ax.set_ylabel('Amount of cereal by manufacture')
ax.set_xlabel('Manufacture')
ax.set_title('Cereal Supply by Manufacture')

plt.show()
reader.close()
