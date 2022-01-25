my_list = list(input('Введите значение без пробела '))

for el in range(1, len(my_list), 2):  # стартуем с первого элемента и берем шаг 2 так как нужна четность
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]
print(my_list)
