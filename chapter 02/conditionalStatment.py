# light = input("Enter the color: ")

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")


# age = 18
# if (age >= 18):
#     print("Apply for licence")
#     print("can vote")

# age = 18
# if (age >= 18):
#     print("Apply for licence")
# else:
#     print("Not apply for licence")

# light = "blue"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("warning")
# elif(light == "green"):
#     print("ok go")
# else:
#     print("light is broken")

# num = 5
# if(num > 2):
#     print("grater than 2")
# if(num > 3):
#     print("greater than 3")

# age = 18
# if(age >= 18):
#     print("can vote")
# else:
#     print("can not vote")

# marks = 54
# if(marks >= 90):
#     print("grade A 1")
# elif(marks >= 80 and marks < 90):
#     print("grade A")
# elif(marks >= 70 and marks < 80):
#     print("grade B")
# elif(marks >= 60 and marks < 70):
#     print("grade C")
# else:
#     print("try again")

# marks = 84
# if(marks >= 90):
#     grade = "A 1"
# elif(marks >= 80 and marks < 90):
#     grade = "A"
# elif(marks >= 70 and marks < 80):
#     grade = "B"
# elif(marks >= 60 and marks < 70):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the student", grade)

# marks = int(input("Enter marks: "))
# if(marks >= 90):
#     grade = "A 1"
# elif(marks >= 80 and marks < 90):
#     grade = "A"
# elif(marks >= 70 and marks < 80):
#     grade = "B"
# elif(marks >= 60 and marks < 70):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the student", grade)

        # Nesting
# age = 84
# if(age >= 18):
#     if(age >= 80):
#         print("you are very old man that's why cannot drive")
#     else:
#         print("can drive")
# else:
#     print("Cannot drive")

# num = int(input("Enter a number: "))

# if num >= 90 and num <= 100:
#     print("Your grade is A 1")
# elif num >= 80 and num <= 89:
#     print("Your grade is B")
# elif num >= 70 and num <= 79:
#     print("Your grade is C")
# elif num >= 60 and num <= 69:
#     print("Your grade is D")
# else:
#     print("Your grade is F")

# name = input("enter student name: ")
# roll_num = input("enter roll number: ")
# num_subject = input("Enter number of subject: ")
# marks = []
# for i in range(num_subject):
#     marks = float(input(f"Enter marks for subject{i + 1}"))
#     marks.append(marks)

# total_marks = sum(marks)
# percentage = total_marks / (num_subject*100)*100
# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 80:
#     grade = "A"
# # elif percentage >= 70:
#     grade = "B"
# elif percentage >= 60:
#     grade = "C"
# elif percentage >= 50:
#     grade = "D"
# else:
#     grade = "F"


# num = float(input("Enter a number: "))
# if num > 0:
#     print("this is a +ve number")
# elif num < 0:
#     print("This is a -ve number")
# else:
#     print("Num is zero")

# fruit = ["Apple", "banana", "orange", "mango", "cherry"]
# fruit.append("grape")
# fruit.append("kiwi")
# for i in fruit:
#     print(i)

# cities = ("karachi", "lahore", "isl")
# print(cities)

# def greet(name):
#     print(f"hello, {name}")
# greet("hamza")
# greet("Nabeel")
# greet("ghani")


# Marksheet code
# name = input("Enter a name: ")
# rollnum = int(input("Enter roll number: "))

# sub1 = int(input("Enter Eng Marks: "))
# sub2 = int(input("Enter Calculus Marks: "))
# sub3 = int(input("Enter ICT Marks: "))
# sub4 = int(input("Enter Pf Marks: "))

# total = sub1 + sub2 + sub3 + sub4
# percentage = total/4

# if percentage >= 90 and percentage <= 100:
#     grade = "A"
# elif percentage >= 80 and percentage <= 90:
#     grade = "B"
# elif percentage >= 70 and percentage <= 80:
#     grade = "C"
# else:
#     grade = "F"
# print(f"/n-----Marksheet-----")
# print(f"Name: {name}")
# print(f"Roll Num: {rollnum}")
# print(f"Subject: {sub1}, {sub2}, {sub3}, {sub4}")
# print(f"Total: {total}")
# print(f"Percentage: {percentage}%")
# print(f"Grade {grade}")


# def addfunc(a, b):
#     return a + b
# a = int(input("enter first number: "))
# b = int(input("enter second number"))
# print(addfunc(a, b))

for i in range(1, 6):
    for j in range(1, 4):
        print(j, end="")
    print()