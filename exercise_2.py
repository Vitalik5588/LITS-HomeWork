''' Задача №2
Розробити функцію *find_most_frequent(text)*, 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає *список слів* (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, “hand-made”). Слова у різних відмінках, числах та з іншими перетвореннями
(наприклад, “page” та “pages”) вважаються різними словами. 
Регістр слів -- навпаки, не має значення: слова “page” та “Page” вважаються 1 словом.

*Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.*

*Наприклад*
Виклик функції: find_most_frequent(‘Hello,Hello, my dear!’)
Повертає: [‘hello’]

Виклик функції: find_most_frequent(‘to understand recursion you need first to understand recursion...’)
Повертає: [‘recursion’, ‘to’, ‘understand’]

Виклик функції: find_most_frequent(‘Mom! Mom! Are you sleeping?!!!’)
Повертає: [‘mom’]
'''


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
