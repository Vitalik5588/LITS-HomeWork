lst = [1,[2,3], 4, [[6,7]]]

test1 = []
for i in lst:
    if type(i) == int:
        test1.append(i)
    elif type(i) == list:
        test1.extend(i)

test2 = []
for i in test1:
    if type(i) == int:
        test2.append(i)
    elif type(i) == list:
        test2.extend(i)

lst = test2

print(lst)
