class Car:
  @staticmethod
  def start():
    print("Car started")

  @staticmethod
  def stop():
      print("Car stopped")

class Toyota(Car):
  def __init__(self, name):
    self.name = name

class Garendi(Toyota):
  def __init__(self, model):
    self.model = model

car1 = Garendi("Garendi Model X")
print(car1.start())