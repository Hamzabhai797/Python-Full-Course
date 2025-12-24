class Car:
  @staticmethod
  def start():
    print("Car started")

  @staticmethod
  def stop():
    print("Car stopped")

class ToyotaCar(Car):
  def __init__(seld, name):
    seld.name = name

car1 = ToyotaCar("Toyota Corolla")
car2 = ToyotaCar("Toyota Camry")
print(car1.name)