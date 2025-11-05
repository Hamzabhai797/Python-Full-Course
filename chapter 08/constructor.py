# class Student:
#   name = "Hamza"
#   def __init__(self):  # constructor
#     print("Constructor called..")
  
# s1 = Student()


# example 2
# class Student:
#   def __init__(self, fullName):  # constructor
#     self.name = fullName
#     print("Constructor called..")
  
# s1 = Student("hamza")
# print(s1.name)

# s2 = Student("Ali")
# print(s2.name)

# example 3
# class Student:

#   def __init__(self, name, marks): 
#     self.name = name
#     self.mark = marks
#     print("Constructor called..")
  
# s1 = Student("hamza", 90)
# print(s1.name, s1.mark)

# s2 = Student("Ali", 85)
# print(s2.name, s2.mark)


#     Default Constructor
class Student:

  def __init__(self):
    print("Constructor called..")

s1 = Student()