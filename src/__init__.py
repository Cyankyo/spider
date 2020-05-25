# import requests
# from bs4 import BeautifulSoup
# if __name__ == '__main__':
#     target = 'https://www.xsbiquge.com/61_61485/3204927.html'
#     req = requests.get(url = target)
#     req.encoding = 'utf-8'
#     html = req.text
#     bs = BeautifulSoup(html, 'lxml')
#     texts = bs.find('div', id='content')
#     print(texts.text.strip().strip('\ufeff').split('\xa0'*4))

import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().strip('\ufeff').split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = '谁把谁当真.txt'
    target = 'https://www.xsbiquge.com/61_61485/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
