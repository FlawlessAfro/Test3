import random

dice = [1,2,3,4,5,6]
n_dices = 5
rand_dices = random.choices(dice, k = n_dices)

print(rand_dices)

new_list = sorted(rand_dices)
print(min(rand_dices))
print(max(rand_dices))
print(new_list)



if rand_dices[0] == rand_dices[1] == rand_dices[2] == rand_dices[3] == rand_dices[4] == rand_dices[5]:
    print("Yatzee!")
