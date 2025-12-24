# class Student:
#   def __init__(self, phy, chem, math):
#     self.phy = phy
#     self.chem = chem
#     self.math = math
#     self.percentage = str ((self.phy + self.chem + self.math) / 3) + "%"

# s1 = Student(80, 90, 70)
# print(s1.percentage)

# s1.phy = 83
# print(s1.phy)  
# print(s1.percentage)



class Student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
    # self.percentage = str ((self.phy + self.chem + self.math) / 3) + "%"

  @property
  def percentage(self):
    return str ((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(80, 90, 70)
print(s1.percentage)

s1.phy = 87 
print(s1.percentage)