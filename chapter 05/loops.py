# while loop

# count = 1
# while count <= 5:
#     print("Hello Hamza")
#     count += 1

# i = 1
# while i <= 100:
#     print("Hi! hamza")
#     i += 1

# i = 1
# while i <= 50:
#     print(i)
#     i += 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1




# print("Sindh madressatul Islam university")
# print("Hamza Khan")

# tup1 = (12, 34.56);

# tup2 = ('abc', 'xyz');
# #Following action is not valid for tuples

# #tup1[0] = 100;

# #So let's create a new tuple as follows tup3 = tup1 + tup2;

# print(tup1 + tup2)


# tup = ('physics', 'chemistry', 1997, 2000);

# print(tup);
# del tup;

# print("After deleting tup : ");

# print(tup);


# LAB 1 class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display_info(self):
        print("Person Info:")
        print(f"  Name  : {self.name}")
        print(f"  Age   : {self.age}")
        print(f"  Height: {self.height} cm")

class Student(Person):
    def __init__(self, name, age, height, roll_no, grade):
        super().__init__(name, age, height)  
        self.roll_no = roll_no
        self.grade = grade

    def display_student(self):
        print("Student Info:")
        print(f"  Roll No: {self.roll_no}")
        print(f"  Grade  : {self.grade}")

student1 = Student("Hamza", 21, 155, "9A-025", "A")

student1.display_info()      
student1.display_student()    





# time = 5:37:00