def ex1(a, b):
  try:
    num = a / b
    return num
  except ZeroDivisionError:
    return ZeroDivisionError


print(ex1(int(input("Ведите первое число ")), int(input("Введите второе число "))))
