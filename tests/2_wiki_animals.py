import requests
import re
import bs4


def animals_dict_by_first_letter_from_wiki() -> dict:
    """
    A function-parser
    It takes list of animals ordered by first letter from wikipedia
    and returns a dict with:
        key - letter of russian alphabet,
        value - count of animals by this letter

    It may take a couple of minutes to see function result
    :return: dict
    """

    animal_list = []
    animal_dict = {}

    for letter in range(ord('А'), ord('Я')):
        response = requests.get(
            f'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from={chr(letter)}')
        page = bs4.BeautifulSoup(response.text, 'html.parser')
        check_letter = page.find(id='mw-pages').find_all('h3')[0].get_text()

        while check_letter == chr(letter):
            tags_a_list = page.find(id='mw-pages').find_all(href=re.compile(r'\/wiki\/.+'))

            for tag in tags_a_list:
                if tag.get_text().startswith(chr(letter)):
                    animal_list.append(tag.get_text())
                else:
                    break
            next_page = page.find(id='mw-pages').find_all("a", string="Следующая страница")[0].get('href')
            go_to_next_page = requests.get(f'https://ru.wikipedia.org{next_page}')
            page = bs4.BeautifulSoup(go_to_next_page.text, 'html.parser')
            check_letter = page.find(id='mw-pages').find_all('h3')[0].get_text()

        animal_dict[chr(letter)] = len(animal_list)
        animal_list = []

    return animal_dict


for char, count_of_animals in animals_dict_by_first_letter_from_wiki().items():
    print(char, ':', count_of_animals)
