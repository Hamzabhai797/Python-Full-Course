class A:
  varA = "wellcome to a"
class B:
  varB = "wellcome to b"
class C(A, B):
  varC = "wellcome to c"

obj = C()
print(obj.varA)
print(obj.varB)
print(obj.varC)