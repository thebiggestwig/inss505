def grade_avg(exam_list):
    return sum(exam_list) / len(exam_list)


# this function is included to calculate the average of input values

def grade_scale(exam_score):
    if exam_score > 89:
        return "A"
    elif exam_score > 79:
        return "B"
    elif exam_score > 69:
        return "C"
    elif exam_score > 59:
        return "D"
    else:
        return "F"


# this function is used to define the range for each letter grade

num = 12
exam_list = []

# this is used to define the number of inputs for the grades array

for int in range(num):
    score = float(input("Please enter your score for Exam {}/12: ".format(int + 1)))
    exam_list.append(score)

# this parameter is used to add the values together as input

examAverage = grade_avg(exam_list)
finalGrade = grade_scale(examAverage)

# this provides variables for the calculations

print(finalGrade)
print(examAverage)

# this returns the desired output to the user once all inputs made
