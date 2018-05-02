''' Задача №3
Розробити функцію *my_sort(func, array, reversed)*
яка приймає два аргументи функцію-ключ (за допомогою якої здійснюється порівняння) та одновимірний масив однотипних даних

*Описати функцію за допомогою анотації типів та рядка документації (включно з параметрами)*
*Наприклад*
Виклик функції: my_sort([‘Aa’, ‘cCc’, ‘bbbbb’, ‘a’])
Повертає: [‘Aa’, ‘a’, ‘bbbbb’, ‘cCc’]

Виклик функції: my_sort([‘Aa’, ‘cCc’, ‘bbbbb’, ‘a’], reverse=True)
Повертає: [‘cCc’, ‘bbbbb’, ‘a’, ‘Aa’]

Виклик функції: my_sort(lambda x: len(x), [‘Aa’, ‘cCc’, ‘bbbbb’, ‘a’])
Повертає: [‘a’, ‘Aa’, ‘cCc’, ‘bbbbb’]

При передачі невірних даних викликати помилку TypeError
Обробити виняткові ситуації та повідомити про них користувача
'''


def my_sort(array: list, reverse:bool =True ) -> list :
    """ Sorts the list for growth and decline.

     Keyword arguments:
         array -- one-dimensional array of data of the same type
         reverse = True -- Sorts the list for growth.
         reverse = False -- Sorts the list for decline.
    """

    dic = {}
    for i in array:
        first_letter = []
        first_letter.append(str(ord(i[0])))   # Записуємо першу букву кожного слова у вигляді цифри
        dic[str(first_letter[0])]= str(i)    #формуємо словник із цифри : слово

    if reverse == True:
        sorted_list = []
        for a in range(len(dic)):
            sorted_list.append(dic.pop(str(min(dic)))) #сортування по мін значеннях ключів
    else:
        sorted_list = []
        for a in range(len(dic)):
            sorted_list.append(dic.pop(str(max(dic))))  # сортування по мax значеннях ключів

    return sorted_list

print(my_sort(['Aa', 'cCc', 'bbbbb', 'a']))
# НЕ ЗРОБИВ!
#-При передачі невірних даних викликати помилку TypeError
#-Обробити !виняткові! ситуації та повідомити про них користувача
