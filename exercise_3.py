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
