
def count_holes(n):
    if isinstance(n, float):
        return 'ERROR'
    try:
        answers = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
        con = 0
        n = int(n)
        n = str(n)
        for i in n:
            if i in answers:
                con += answers.get(i)
        return con
    except ValueError:
        return "ERROR"
    except TypeError:
        return "ERROR"

print(count_holes('81'))
