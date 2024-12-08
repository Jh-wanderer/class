# 정적페이지 웹스크래핑
# 1. 정적페이지 - 요청한 url에서 응답받은 html을 그대로 사용한 경우
#   - 서버사이드렌더 : 서버에서 html을 생성 / 대표적 예시 네이버 웹소설 - 페이지 소스 보기, 그대로 1대1 내용

# 2. 동적페이지 - 요청한 url에서 응답받은 html 내부의 javascript을 실행해서 html을 새로 만든 경우
#   - 클라이언트사이드렌더 : 클라이언트에서 html을 생성 / 대표적 예시 네이버 웹툰 - 페이지 소스 보기 / F12 = 개발자 도구 open

import requests
import bs4

print(requests.__version__) # 2.32.3
print(bs4.__version__) # 4.12.3

# requests
# 파이썬에서 http요청(웹)을 쉽게 작성할 수 있다.
def web_request(url):
    response = requests.get(url)
    # # print(response) -> <Response [200]>
    # print(response.status_code)
    # print(response.text)
    return response.txt

url = 'https://www.naver.com'

# beautifulsoup
# html, xml을 parsing(쪼개서 분석)해서 데이터 추출
from bs4 import BeautifulSoup
with open('../01_html/sample.html', 'r', encoding='utf-8') as f:
    html = f.read()
bs = BeautifulSoup(html,'html.parser')
# print(type(bs))
# print(bs)

# find, find all
# def test_find():
#     tag = bs.find('li')
#     print(tag)
#
#     tags = bs.find_all('section', {'id' : 'section1'}, )
#  # 첫번째 검색어는 저걸 가지고 있는 것을 다 찾아옴, id를 지정하는 경우는 그게 정확하게 포함하는 경우 데려옴
#     print(len(tags))
#     print(tags)
# test_find()

# def test_select():
    # -CSS 선택자 : 특정 태그를 찾기 위한 표현식
    # - 태그명 그대로 사용
    # - id #아이디
    # - class .클래스
    # tag = bs.select_one('section#section2') # 클래스 대략 검색
    #print(type(tag))
    #print(tag)
    # tags = bs.select('.section-content#section3') # 클래스 지칭 검색
    # print(tags)

# test_select()

# def get_content():
#     # section#section2 > h2 : 직계자식 태그
#     # section#section2 li: 후손 태그
#     tags = bs.select('section#section2 li')
#     # tags = bs.select('section#section2>h2')
#
#     print('h2 :', tags)
#
#     for tag in tags:
#         print(tag.text) # 태그는 날리고, 그 안의 글자만 달라.

# get_content()

def get_content2():
    h2_tag = bs.select_one('section#section1 p') # p는 두줄 있으나 첫줄만 우선 가져옴
    # print('h2 : ', h2_tag.text)
    # for h2_tag in h2_tag:
    print('h2_tag :', h2_tag.text)

    p_tags = bs.select('section#section1 p')
    for p_tag in p_tags:
        print('p_tags :', p_tag.text)


get_content2() #이거 해야함 안하면 완료가 안됨


def get_content3():
    # 자식태그 조회
    section1_tag = bs.select_one('section#section1')
    # 특정태그 하위에서 조회
    h2_tag = section1_tag.select_one('h2') # 위에서 한번 명시한 것을 굳이 안해도 됨
    print('h2_tag :', h2_tag)


    # 모든 자식태그 조회
    children = section1_tag.findChildren()
    print('children :', children)

    for child in children:
        print('child :', child.text)

get_content3()

