# class Student:  # class banayi Student naam sa
#   name = "Hamza"

# s1 = Student() # object banaya Student class ka
# print(s1.name)
# s2 = Student()
# print(s2.name)

# example 2
# class Car:
#   color = "Red"
#   model = "2020"
#   brand = "Toyota"
# car1 = Car()
# print(car1.color)
# print(car1.model)
# print(car1.brand)


# Methods
class student:   # class banayi student naam sa
  def __init__(self):  # constructor define kiya
    self.name = "Hamza"  # instance attribute define kiya name naam sa (ya object attribute hay)
    self.age = 20

  def greet(self):    # method define kiya greet naam sa
      print("Hello, my name is " + self.name)

  def display_age(self):  # method define kiya display_age naam sa
      print("I am " + str(self.age) + " years old.")
s1 = student()
s1.greet()
s1.display_age()