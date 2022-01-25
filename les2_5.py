my_list = [7, 5, 3, 3, 2]
new_score = int(input("введите номер "))
a = 0
for n in my_list:
    if new_score <= n:
        a += 1
    else:
        break
my_list.insert(a, new_score)
print(my_list)

