new_list = []
for i in range(11, 80):
    if i % 3 == 0 and i % 5 == 0:
        new_list.append("$$@@")
    elif i % 3 == 0:
        new_list.append("$$")
    elif i % 5 == 0:
        new_list.append("@@")
    else:
        new_list.append(i)
print(new_list)