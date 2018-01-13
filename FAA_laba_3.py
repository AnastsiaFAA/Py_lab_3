#3. Используя Python и модуль requests и bs4 написать скрипт,
# извлекающий новости (отдельно заголовок, анотацию, авторов)
# из веб-страницы новостного агенства (напр. washingtonpost.com).
# Требуется использовать поиск по дереву html, а не регулярные выражения
from bs4 import BeautifulSoup
import requests

def main():
    PageHTML = requests.get("https://pikabu.ru/").text
    Soup = BeautifulSoup(PageHTML, "html.parser") #док. как влож.стр-ра данных

    for i in Soup.find_all("div", "story__main"):   # ищет новости

        print("\n\t\t\t***\n")   
        
        tagos = []

        for titles in i.find_all("a", "story__title-link "):   # заголовог
            title = titles.get_text()
            print("Title:", title)

        for tags in i.find_all("a", "story__tag"):       # тэги
            tag = tags.get_text()
            tagos.append(tag[9:-8])   # список тэгов без лишних символов
        print('Tags:', tagos)

        for authors in i.find_all("a", "story__author"):      # автор
            author = authors.get_text()
            print('Author:', author)


main()
