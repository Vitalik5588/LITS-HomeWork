

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