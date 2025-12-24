class P():
  name = "noor ul islam"
  def Show(self):
    print("My name is", self.name)

class Son1(P):
  def Display(self):
    print("My name is Hamza", self.name)

class Son2(P):
  def Show(self):
    print("My name is Osama", self.name)

s1 = Son1()
s2 = Son2()
s1.Display()
s2.Show()