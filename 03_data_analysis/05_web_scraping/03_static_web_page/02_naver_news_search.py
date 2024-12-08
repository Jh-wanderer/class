# 1. request url 요청
# 2. html 응답
# 3. BeautifulSoup 객체를 생성
# 4. 태그 조회 (n개)
# 5. 반복 순회
# 6.

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime

# 검색 url 생성
query = "배달앱 평점"
url = f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sort=1&query={query}' #인기순은 sort=0, 최신순은 sort=1

# 뉴스 검색 요청
response = requests.get(url)
html = response.text
print(html)

# html parsing : BeautifulSoup 객체 만들기(받은 html을 주고)
bs = BeautifulSoup(html, 'html.parser')
print(bs)

# 뉴스 블럭 가져오기 (title, href, img.thumb)
news_contents = bs.select('div.news_contents')
# print(len(news_contents))

# 스크랩한 뉴스 정보를 담을 NewsEntry
class NewsEntry:
    def __init__(self, title, href, img_path):
        self.title = title
        self.href = href
        self.img_path = img_path

    def __repr__(self):
        return f'NewsEntry(title={self.title}, href={self.href}, img_path={self.img_path})'

news_entries = []

def img_download(img_lazysrc, i):
    img_dir = './images'  # 경로 설정
    today = datetime.now().strftime('%y%m%d')
    filename = f'{img_dir}/{today}_{i}.jpg'
    urlretrieve(img_lazysrc, filename)
    return filename

for i, news_content_tag in enumerate(news_contents):
    a_tag = news_content_tag.select_one('a.news_tit')
    title = a_tag.text
    href = a_tag['href']
    print(title, href)

    img_tag = news_content_tag.select_one('img.thumb')
    img = None # 이미지 내역 초기화
    if img_tag:
        img_lazysrc = img_tag['data-lazysrc']
        if img_lazysrc.startswith('http'):
            img = img_download(img_lazysrc, i) # 이미지 다운로드 처리(함수 호출)

news_entry = NewsEntry(title, href, img)
news_entries.append(news_entry)

for news_entry in news_entries:
    print(news_entry)

# 뉴스 블럭 접근
# 하이퍼링크-제목은 주로 a 태그
# a_tags = bs.select('a.news_tit')
# print(len(a_tags))
#
# for a_tag in a_tags:
#     title = a_tag.text
#     href = a_tag['href']
#     print(title, href) # 들여쓰기 안하며  마지막 것만 나옴

print('---------------------------------------------------------')


# 뉴스 썸네일 이미지 가져오기
# - 이미지 url 가져와서, 다운로드
# img.thumb 태그를 찾아서 src속성 가져오기
# #
# img_tags = bs.select('.news_contents img.thumb')
# img_lazysrc = []
#
# for img_tag in img_tags:
#     print(img_tag['src']) # img 와 txt를 따로 가져오려다 보니 (비동기 처리) src를 직접 가져와도 url이 가져와지지 않는다. 대신 틀 부분이 가져와짐.
#     # img url은
# #     # print(img_tag)
#
# for img_tag in img_tags:
#
#     # print(img_tag['data-lazysrc'])
#     img_lazysrc.append(img_tag['data-lazysrc'])
#
# # print(img_lazysrc)
# #
# # # 이미지 다운로드
# #  img_dir ='./images' # 경로 설정
# #
# # today = datetime.now().strftime('%y%m%d')
# #
# # for i, src in enumerate(img_lazysrc):
# #     if src.startswith('http'):
# #         urlretrieve(src, f'{img_dir}/{today}_{i}.jpg') # /는 그 안 위치
#
#
# # 뉴스 블럭 가져오기
# news_contents = bs.select('div.news_contents')
# print(len(news_contents))
#
# # def img_download(img_lazysrc, i):
#     img_dir = './images'  # 경로 설정
#     today = datetime.now().strftime('%y%m%d')
#     filename = f'{img_dir}/{today}_{i}.jpg'
#     urlretrieve(img_lazysrc, filename)
#     return filename

# for i, news_content_tag in enumerate(news_contents):
#     a_tag = news_content_tag.select_one('a.news_tit')
#     title = a_tag.text
#     href = a_tag['href']
#     print(title, href)

    # img_tag = news_content_tag.select_one('img.thumb')
    # img = None
    # if img_tag:
    #     img_lazysrc = img_tag['data-lazysrc']
    #     if img_lazysrc.startswith('http'):
    #         img = img_download(img_lazysrc, i)
    # print(title, href, img)

