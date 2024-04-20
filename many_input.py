entered_list = input("Введите список чисел через пробел").split()

num_list = [int(i) for i in entered_list]

print("Список чисел: ", num_list)