# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no = acc_no
#     self.acc_pass = acc_pass

# acc = Account("123456", "mypassword")
# print(acc.acc_no)
# print(acc.acc_pass)

            # private
# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass

# acc = Account("123456", "mypassword")
# print(acc.acc_no)
# print(acc.__acc_pass)



# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass

#   def reset_pass(self):
#     print(self.__acc_pass)

# acc = Account("123456", "mypassword")
# print(acc.acc_no)
# print(acc.reset_pass())