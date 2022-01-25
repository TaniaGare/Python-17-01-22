my_list = input('Введите строку разделяя пробелами ').split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[0:11])
