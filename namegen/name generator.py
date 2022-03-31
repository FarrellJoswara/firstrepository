import random
names = [] 
with open(r"namegen\names.txt") as f:
    names = f.readlines()

print(names[random.randint(0, len(names))].strip())