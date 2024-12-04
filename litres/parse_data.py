from bs4 import BeautifulSoup
import requests
from .models import LitresModel


def parse():
    URL = 'https://www.litres.ru/popular/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_books = soup.findAll('div', class_='ArtDefault_container__0yjZl')
    list_books = list()
    for data in all_books:
        books = dict()
        books['img'] = data.find('img', class_='AdaptiveCover_image__eAZyi').get('src')
        books['name'] = data.find('p').text
        books['author'] = data.find('a', class_='ArtInfo_author__0W3GJ').text
        books['price'] = data.find('strong').text
        list_books.append(books)
    return(list_books)

def create_data():
    data_list = parse()
    for item in data_list:
        if not LitresModel.objects.filter(name=item.get('name')):
            LitresModel.objects.create(
                name=item.get('name'),
                author=item.get('author'),
                price=item.get('price'),
                img=item.get('img'),
            )
        else:
            print(f"[ LOG ] == '{item.get('name')}' is already exists!")
    


