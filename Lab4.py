import math

# step 2: this is a for loop

for i in range(0,10):
    print(i)

# step 3: this is a while loop

i = 1
while i <= 10:
    print(i)
    i+= 1

# step 4: this is a while loop that increments at +2

i = 1
while i <= 10:
    print(i)
    i+= 2

# step 5-7: this uses the math function to get pi then multiplying it by radius value input squared

radius = float(input("Enter your radius: "))
area = math.pi * radius * radius

print(area)

# step 8-10: getting the users length and width values

length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
area2 = length * width

print(area2)