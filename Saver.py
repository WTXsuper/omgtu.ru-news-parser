from datetime import datetime

def save(lst: list):
headings_formatted = '\n'.join(lst)  # превращаем список в строку с построчным разделителем
with open('OUTPUT.txt', 'w', encoding='utf-8') as F:  # открываем файл на запись
    F.write(datetime.now().strftime("%d.%m.%Y %H:%M") + '\n' + headings_formatted)  # доп. добавил текущ. дату
print("РЕЗУЛЬТАТ СОХРАНЁН В OUTPUT.txt")
