from Parser import parse
from datetime import datetime  # импортируем библиотеку для работу с датой и временем

if __name__ == '__main__':
    headings_formatted = ''.join(parse())  # превращаем список в строку с нулевым разделителем
    with open('OUTPUT.txt', 'w', encoding='utf-8') as F:  # открываем файл на запись
        F.write(datetime.now().strftime("%d.%m.%Y %H:%M") + '\n' + headings_formatted)  # доп. добавил текущ. дату
    print("РЕЗУЛЬТАТ СОХРАНЁН В OUTPUT.txt")
