###############################################################################
#Представлен список чисел. Необходимо вывести элементы исходного списка, 
#значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его 
#формирования используйте генератор.
###############################################################################

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for x in range(len(my_list)-1): #Итак, если мы хотим получить доступ к последнему элементу списка, оператор должен быть записан как lst[len-1]
    if my_list[x] < my_list[x+1]:
        new_list.append(my_list[x+1])
        print(new_list)


