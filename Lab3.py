import math
number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))

print(number1, number2)

sum = number1+number2

print(sum)

difference = number1-number2
multiplication = number1*number2
division = number1/number2

print(difference, multiplication, division)

number3 = int(input('Enter number 3: '))

sum = number1+number2+number3
difference = number1-number2-number3
multiplication = number1*number2*number3
division = (number1/number2)/number3

print(sum, difference, multiplication, division)

print(math.pow(9, 3))

print(math.exp(division))
print(math.floor(division))
print(math.log(sum))
print(math.perm(sum, multiplication))
print(math.tan(difference))
print(math.sqrt(multiplication))
print(math.fmod(multiplication, sum))
print(math.factorial(4))
print(math.fabs(4.2463))
print(math.degrees(57.2))
