from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse():
    news = []
    url = 'https://omgtu.ru/l/?PAGEN_1=1'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print("STATUS CODE:", page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4

    block = soup.findAll('h3', class_='news-card__title')  # находим  контейнер с нужным классом
    for data in block:  # проходим циклом по содержимому контейнера
        news.append(normalize(data.text))


def normalize(text: str):  # преобразуем строку в нормальный вид
    return text.replace('\n', '').strip(' ') + '\n'  # убираем лишние пробелы, перенос строки ставим в конце
