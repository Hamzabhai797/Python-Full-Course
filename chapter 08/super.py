# class Car:
#   def __init__(self, type):
#     self.type = type

#   @staticmethod
#   def start():
#     print("Car started")

#   @staticmethod
#   def stop():
#     print("Car stopped")

# class Toyota(Car):
#   def __init__(self, name, type):
#     self.name = name
#     super(). __init__(type)

# c1 = Toyota("Corolla", "electric")
# print(c1.type)



class Car:
  def __init__(self, type):
    self.type = type

  @staticmethod
  def start():
    print("Car started")

  @staticmethod
  def stop():
    print("Car stopped")

class Toyota(Car):
  def __init__(self, name, type):
    self.name = name
    super(). __init__(type)
    super().start()

c1 = Toyota("Corolla", "electric")
print(c1.type)