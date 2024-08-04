my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n_list = len(my_list)
n = 0
while n <= n_list and my_list[n] >= 0:
    if my_list[n] == 0:
        n += 1
        continue
    else:
        print(my_list[n])
    n += 1
