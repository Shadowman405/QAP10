list1 = [1, 5, 2, 9, 2, 9, 1]

list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)
