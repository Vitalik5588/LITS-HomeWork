''' Задача №4
Розробити функцію *counter(a, b)*, 
яка приймає 2 аргументи -- *цілі невід’ємні числа a та b*, 
та повертає число -- кількість різних цифр числа b, які містяться у числі а.

*Наприклад*
Виклик функції: _counter(12345, 567)_
Повертає: *1*
Виклик функції: _counter(1233211, 12128)_
Повертає: *2*
Виклик функції: _counter(123, 45)_
Повертає: *0*
'''


def clean_list(l):                    # Розбиває вхідні дані і створює список із їх унікальних значень
    output_list=[]
    for i in l:
        if i not in output_list:
            output_list.append(i)
    return(output_list)

def counter(a , b):
    if isinstance(a, int) and isinstance(b, int):
        a = str(a)
        b = str(b)
        con = 0
        for i in clean_list(b):             # Порінює списки a та b на повторюючі числа
            if i in clean_list(a):          # і рахує їх кількість
                con+=1
        return(con)
    else:
        return "TypeError"

print(counter(1233211, 12128))