def slice_less(my_list, lesser):
    new_list_2 = []
    for i in range(0, len(my_list)):
        if my_list[i] > lesser:
            new_list_2.append(my_list[i])
    new_list_2.sort()
    return new_list_2


print(slice_less([2, 6, 18, 0, 5, 13, -9, 99], 6))


# другий спосіб


def slice_less_2(my_list, lesser):
    new_list_3 = []
    [new_list_3.append(my_list[i]) for i in range(0, len(my_list)) if my_list[i] > lesser]
    new_list_3.sort()
    return new_list_3


print(slice_less_2([2, 6, 9, 0, 5, 12, -19, 99, 54], 7))