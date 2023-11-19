
liste = [23,45,18,7,99,86,74,55,83,2,75]

alpha1 = 0.05

liste = sorted(liste)
print(liste)

print(len(liste))

lower_idx = round((len(liste)*alpha1/2))
upper_idx = round(len(liste)*((1-(alpha1/2)))-1)

print(lower_idx) #Dette er index over hvor i intervallet de kutter upper og lower.
print(upper_idx)