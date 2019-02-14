def intreverse(n):
  rem = ''
  while n >0:
    rem += str(n%10)
    n = n//10
  print(int(rem))
  return
