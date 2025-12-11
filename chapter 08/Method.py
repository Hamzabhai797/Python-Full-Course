# class Student:
#     def __init__(self, Name, marks):
#         self.Name = Name
#         self.marks = marks
        
#     def welcome(self):
#         print("wellcome students", self.Name)
    
# s1 = Student("Hamza khan", 500)
# s1.welcome()


# class Student:
#     def __init__(self, Name, marks):
#         self.Name = Name
#         self.marks = marks
        
#     def welcome(self):
#         print("wellcome students", self.Name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Hamza khan", 500)
# s1.welcome()
# print(s1.get_marks())

class Student:
    def __init__(self, Name, marks):
        self.Name = Name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.Name, "your average is:", sum/4)
        
s1 = Student("Hamza khan", [95, 85, 75, 80])
s1.get_average()