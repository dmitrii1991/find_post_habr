import re
import time

import requests
import xlsxwriter

def habr_post(file_name='1.xlsx', find=None, start=None, end=None, sleep=0,
              find_only_title=False):
    """
    Ищет посты с с метками на хабре (избегает ограничение в 50 страниц). Посты Хабра идут по порядку
    :param file_name: название файла с будущим результат
    :param find: поиск ключевых слов на ХАБРЕ
    :param start: начало диапозона постов
    :param end: конец диапозона постов
    :param sleep: временная блокировка
    :param find_only_title: Поиск только в титуле поста
    :return: None
    """
    url = 'https://habr.com/ru/post/'
    number = start
    pattern = re.compile(r"(<title>)[а-яА-Я  \/_a-zA-Z0-9?.,@#$%^&*()-=—]*(<\/title>)")  # поиск титула страницы

    if start and end and find:
        with xlsxwriter.Workbook(file_name) as workbook:
            worksheet = workbook.add_worksheet('habr')
            worksheet.set_column('A:A', 55)
            worksheet.set_column('B:B', 35)

            row = 0
            while True:
                active_url = url + str(number) + '/'
                time.sleep(sleep)
                text = requests.get(active_url).text
                print(number)
                for i in find:
                    if i in text:
                        title = pattern.search(text)
                        if title:
                            title = title.group()[7:-8]
                            if (find_only_title and set(find) & set(title.split())) or find_only_title is False:
                                worksheet.write(row, 0, title)
                                worksheet.write(row, 1, active_url)
                                row += 1
                                break
                        else:
                            break
                if number == end:
                    break
                number -= 1


if __name__ == '__main__':
    st = time.time()
    habr_post(start=430_000, end=429_990, find=['Питон', 'питон', 'Python', 'python'])
    print(time.time() - st)
