from Parser import parse  # импортируем основную функцию parse() из Parser
from datetime import datetime  # импортируем библиотеку для работы с датой и временем

if __name__ == '__main__':
    headings_formatted = '\n'.join(parse())  # превращаем список в строку с построчным разделителем
    with open('OUTPUT.txt', 'w', encoding='utf-8') as F:  # открываем файл на запись
        F.write(datetime.now().strftime("%d.%m.%Y %H:%M") + '\n' + headings_formatted)  # доп. добавил текущ. дату
    print("РЕЗУЛЬТАТ СОХРАНЁН В OUTPUT.txt")
