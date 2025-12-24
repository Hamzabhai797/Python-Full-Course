class Account:
  def __init__(self, balance, acc_no):
    self.balance = balance
    self.acc_no = acc_no

  # debit method
  def debit(self, amount):
    self.balance -= amount
    print("RS ", amount , " debited from your account")
    print("Available balance is RS ", self.balance)

  # credit method
  def credit(self, amount):
    self.balance += amount
    print("RS ", amount , " credited to your account")
    print("Available balance is RS ", self.balance)

  def get_balance(self):
    return self.balance

acc1 = Account(10000, 12345)
acc1.debit(2000)
acc1.credit(5000)