# name = input("enter first name: ")
# print(len(name))

# str = "hi, $am the $ symbol"
# print(str.count("$"))

# str = "HAMZA"
# print(str.lower())

# str = "HAMZ\tA"
# print(str.strip()) # strip function remove the white space from the start and end of the string

# str = "HAMZA bhai is a best teacher"
# print(str.replace("HAMZA", "osama"))

# str = "HAMZA bhai is a best teacher"
# print(str.startswith("H"))

# str = "HAMZA bhai is a best teacher"
# print(str.endswith("r"))

# str = "HAMZA bhai is a best teacher"
# print(str.capitalize())

# num = int(input("Enter Number: "))
# if(num % 2 == 0):
#     print("This is even number")
# else:
#     print("This Number is not even")

# num = int(input("Enter a number: "))
# if(num % 2 != 0):
#     print("This number is odd")
# else:
#     print("This number is even")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if(a >= b and a >= c):
#     print("A is greater", a)
# elif(b >= a and b >= c):
#     print("B is greater:", b)
# else:
#     print("C is greater:", c)

# num = int(input("Enter a number: "))
# if(num % 7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not multiple of 7")

marks = int(input("Enter marks: "))
if(marks >= 90 and marks <= 100):
    print("Grade A 1")
elif(marks >= 80 and marks <= 90):
    print("Grade A")
elif(marks >= 70 and marks <= 80):
    print("Grade B")
elif(marks >= 60 and marks <= 70):
    print("Grade C")
elif(marks >= 50 and marks <= 60):
    print("Grade D")
else:
    print("Grade F")
