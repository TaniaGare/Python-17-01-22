def ex3(a, b, c):
    list_minn = [a, b, c]
    list_minn.remove(min(a, b, c))

    return sum(list_minn)


print(ex3(76, 9, 17))

 
