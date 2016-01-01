from requests import get
from bs4 import BeautifulSoup as BS

url = 'http://www.aelf.org/office-messe'
url = 'http://www.aelf.org/office-messe?date_my=13/01/2016'


def get_text(soup, type_text):
    """type_text in {'1ère lecture', 'Psaume', '2ème lecture', 'Evangile'}"""
    html_text =  soup.find(name='div', attrs={'id': type_text})
    if html_text == None:
        return ''
    if type_text == 'Psaume':
        titre = 'Psaume'
    elif type_text == 'Evangile':
        titre = html_text.find_all('p')[1].b.i.string
    else:
        titre = html_text.p.b.i.string

    text = "\n".join(html_text.find(name='div', attrs={'class': 'content'})
                     .p.strings)
    return "{}\n{}\n".format(titre, text)


def main():
    response = get(url)
    soup = BS(response.text, "html5lib")
    type_texts = ['1ère lecture', 'Psaume', '2ème lecture', 'Evangile']
    for type_text in type_texts:
        yield get_text(soup, type_text)
    # yield soup
