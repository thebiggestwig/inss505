import random

# this imports the random functions necessary for the solution

num_list = []

# this creates an array that holds all 1000 desired random numbers

for int in range(0, 1000):
    num = random.randint(0, 1000000)
    num_list.append(num)

# this allows the 1000 random numbers generated from the range of 0-1000000 to be strung together

print(num_list)

# this function prints the final array of 1000 random numbers
