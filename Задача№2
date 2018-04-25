
def find_most_frequent(text):

    text = text.lower() 		 # Перетворюємо у нижній регістр
    rewritten_text = ""
    box = []

    for i in text:				# Вибираємо слова, а символи замінюємо на пробіл
        if i.isalnum() == True:
            rewritten_text = rewritten_text + i
        else:
            rewritten_text = rewritten_text + " "
    rewritten_text = rewritten_text.split()
    
    for i in rewritten_text:		# Вибираємо слова,які повторюються більше 1 разу
        if rewritten_text.count(i)> 1:
            box.append(i)
           
    box = set(box)			# Позбулися повторювань слів 
    box = list(box)
    box.sort()				# Сортуємо в алфавітному порядку

    return box


print (find_most_frequent("Mom! Mom! Are you sleeping?!!!"))
