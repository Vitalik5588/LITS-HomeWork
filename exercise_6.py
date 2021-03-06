''' Задача №6
*Вхідні дані:* рядок, передається як аргумент функції. Може містити пробіли, літери латинського алфавіту в будь-якому регістрі та цифри.

*Результат роботи:* рядок “YES”, якщо отриманий рядок є паліндромом, або “NO” - якщо ні. Рядок вважається паліндромом, якщо він однаково читається як зліва направо, так і справа наліво. Відмінністю регістрів та пробілами знехтувати.

_Наприклад_
*Вхідні дані:* 0
Результат: YES
*Вхідні дані:* puppy
Результат: NO

*Вхідні дані:* “mystring1Gni rts ym”
Результат: YES
'''


def polindrom(s):
    s = s.lower()                # Перетворює текст в малі символи
    format_str = ""

    for i in s:                  # Позбуваємся пробілів
        if i == " ":
            continue
        else:
            format_str+= i

    helf = len(format_str)/2                # Вираховуємо половину довжини слова
    helf1= int(helf)
    try:
        if helf % helf1 == 0:               # У випадку коли довжина слова парна
            case1 = format_str[:helf1]      # Записуємо першу половину слова
            case2 = format_str[:helf1-1:-1] # Записуємо реверс другої половини слова
            if case1 == case2:
                return "YES"
            else:
                return "NO"
        else:                               # У випадку коли довжина слова непарна
            case1 = format_str[:helf1+1]
            case2 = format_str[:helf1-1:-1]
            if case1 == case2:
                return "YES"
            else:
                return "NO"
    except ZeroDivisionError:               # У випадку якщо у нас слово із 1 символа
        return "YES"


print(polindrom("mystring1Gni rts ym"))