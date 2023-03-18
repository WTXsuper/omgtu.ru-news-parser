from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse() -> list:
    headings = []  # список для хранения заголовков
    page_counter = 1  # счётчик страниц
    news_amount = parse_amount()  # находим количество статей

    while (len(headings) < news_amount):  # перебираем все страницы
        url = 'http://omgtu.ru/l/?PAGEN_1=' + str(page_counter)  # передаем URL-адрес сайта Политеха + нужную страницу
        page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
        if page.status_code != 200:  # проверка на доступность omgtu.ru
            print("ОШИБКА! Не удалось подключиться к omgtu.ru")
            exit(1)
        soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
        block = soup.findAll('h3', class_='news-card__title')  # находим  контейнер с нужным классом
        for data in block:  # проходим циклом по содержимому контейнера
            text = normalize(data.text)
            headings.append(text)  # добавляем обработанный текст заголовка в список
        page_counter += 1  # переходим к следующей странице

    print("СТРАНИЦ:", page_counter - 1)
    print("ОБРАБОТАНО ЗАГОЛОВКОВ:", len(headings))
    return headings


def normalize(text: str) -> str:  # преобразуем строку в нормальный вид
    return text.replace('\n', '').strip(' ') + '\n'  # убираем лишние пробелы, перенос строки ставим в конце


def parse_amount() -> int:
    amount = 0
    url = 'http://omgtu.ru/l/'  # передаём URL сайта Политеха
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    if page.status_code != 200:  # проверка на доступность omgtu.ru
        print("ОШИБКА! Не удалось подключиться к omgtu.ru")
        exit(1)
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    block = soup.findAll('font', class_='text')  # находим  контейнер с нужным классом
    for data in block:
        pointer = data.text.find("из")  # ищем кодовое слово 'из' (страница xxx из xxx )
        if pointer == -1:  # если в текущем блоке не найдено, идём к следующему
            break
        amount = int(data.text[pointer + 3::])  # делаем срез и конвертируем в число
    print("НАЙДЕНО СТАТЕЙ:", amount)
    return amount
