def audit(x,y):
    a = x
    b = y
    while True:
        if a is b:
            a += 1
            b += 1
        else:
            end = a
            break
    a = x
    b = y
    while True:
        if a is b:
            a -= 1
            b -= 1
        else:
            start = a
            break
    return "start = {} and end = {}".format(start,end)


print(audit(0,0))