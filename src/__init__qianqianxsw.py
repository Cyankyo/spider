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
import re


def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().strip('\ufeff').split('\xa0' * 4)
    return content


def next_page():
    print('aa')


if __name__ == '__main__':
    server = 'https://www.qianqianxsw.com'

    target = 'https://www.qianqianxsw.com/203/203886/'
    req = requests.get(url=target)
    req.encoding = 'gbk'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    book_name = chapter_bs.find('h1').text
    print(book_name)
    book_author = chapter_bs.find('h3').find('a').text
    print(book_author)
    txt_name = book_name + 'by' + book_author + '.txt'
    chapters = chapter_bs.find_all('ul', attrs={'class': 'list-group list-charts'})
    chapters = chapters.pop(1)
    first_chapter = chapters.find('a')
    url = server + first_chapter.get('href')
    while url is not None:
        req = requests.get(url=url)
        req.encoding = 'gbk'
        page_html = req.text
        page_bs = BeautifulSoup(page_html, 'lxml')
        content = page_bs.find('div', id='content-txt')
        content = (content.text.strip().strip('\ufeff').strip('\xa0' * 4)
                   .strip('收藏网址下次继续看："qianqianxsw.com"。')
                   .strip('阅读提示：系统检查到无法加载当前章节的下一页内容，请单击屏幕中间，点击右下角或者右上角找到“关闭畅读”按纽即可阅读完整小说内容。')
                   .strip('本章未完，点击下一篇继续阅读！').strip('请记住本站域名:"qianqianxsw.com"    一秒记住域名:"qianqianxsw．com"')
                   .strip('"'+book_name+'"'+'最新章节请访问 千*千*看*书'+target)
                   .strip('\n\r')
                   )
        # print(content)
        chapter_name = page_bs.find_all('div', attrs={'class': 'panel-heading'}).pop(0).text
        print(chapter_name)
        with open(txt_name, 'a', encoding='utf-8') as f:
            if re.match(r'/', chapter_name) == None:
                f.write('\n')
                f.write(chapter_name)
                f.write('\n')
            f.write(content)
        # 整下一页
        next_button = page_bs.find('ul', attrs={'class': 'pager'}).find_all('script').pop(1)
        pattern = re.compile('([0-9]|-)+.html')
        # print('next_button' + next_button.string)
        a = re.search(pattern, next_button.string)
        # url=None
        if a and a.group() != '0.html':
            url = target + a.group()
        else:
            url = None
