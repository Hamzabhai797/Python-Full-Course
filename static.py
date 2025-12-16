class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello, welcome to the Student class!")

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print(f"Average marks of {self.name} is {total / len(self.marks)}")

s1 = Student("Hamza", [90, 80, 70])
s1.hello()
s1.get_avg()

