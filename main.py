from Parser import parse  # импортируем основную функцию parse() из Parser
from Saver import save
from datetime import datetime  # импортируем библиотеку для работы с датой и временем

if __name__ == '__main__':
    save(parse())
