a = int(input('Введите цифру 1 до 12 включительно '))
month = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень",
         "Зима"]
id_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

month_dictionary = dict(zip(id_month, month))
print(month_dictionary.get(a))
