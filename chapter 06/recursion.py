def show(n):
  if n == 0:
    return
  print(n)
  show(n-1)
show(5)

# time 6:52:30