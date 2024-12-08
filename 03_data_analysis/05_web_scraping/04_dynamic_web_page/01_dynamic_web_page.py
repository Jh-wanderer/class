# selenium
# 웹 어플리케이션 UI테스트 도구로써, python, java, c#, ruby등을 지원
# 특정 웹 페이지와 상호작용하며, 데이터의 입출력, 브라우저 내 여러 이벤트를 지원한다.

# - 인증을 요구하는 특정 웹 페이지의 데이터를 스크랩
# - 무한 댓글 스크랩
# - 브라우저용 매크로로써 사용 가능

import selenium

from selenium import webdriver

# 키보드 입력
from selenium.webdriver.common.keys import Keys

# 태그 조회 방식(id, class_name, css_selector, x_path)
from selenium.webdriver.common.by import By

# 스크롤 처리 등
from selenium.webdriver import ActionChains


# 지연 대기
import time

print(selenium.__version__) # 4.27.1

# 1. 크롬 실행(드라이버 설치) - 드라이버를 코드를 짤 파이썬 파일이 있는 부모파일에 넣고 진행
path = 'chromedriver.exe' # 같은 위치
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 2. url 특정 사이트 접속
driver.get('https://www.naver.com')
time.sleep(2)

# 3. 사전처리 : 검색어 입력 & 버튼 클릭
search_box = driver.find_element(By.ID, 'query')

search_box.send_keys('스타벅스 md') # keys는 맨 위에 있듯이, 키보드 입력 부분이라 여기에서는 검색하는 절차로 볼 수 있다.

search_box.send_keys(Keys.RETURN) # keys.이후 부분은 우리 키보드에 있는 걸 그대로 따옴

time.sleep(2) # 이정도 시간을 각각 줌

# 뉴스 카테고리로 보게 하기. > 버튼 클릭 후 뉴스 클릭

right_btn = driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span') # 원하는 부분의 개발자 코드 파트에서 우클릭 - copy - xpath
right_btn.click()

time.sleep(2)

# 뉴스버튼

x_path = '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[8]/a' # xpath를 데려와서 변수 처리

news_btn = driver.find_element(By.XPATH, x_path)
news_btn.click()

time.sleep(2)

# 4. 스크롤 처리 : 화면 스크롤 후 더 많은 데이터 확보 / 개발자 도구에서, 스크롤은 body tag 파트를 봐야 함

for _ in range(4): # 그저 반복만 하는 경우 _ 사용 가능
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END) # END키는 맨 아래로 스크롤하는 효과
    time.sleep(2)

# 5. WebElement 접근 & 데이터 추출

news_contents_elems = driver.find_elements(By.CSS_SELECTOR, '.news_contents')
print(len(news_contents_elems))

for news_content_elem in news_contents_elems :
    #print(news_content_elem.text) # text 안해주면 주소 형식
    a_tag = news_content_elem.find_element(By.CSS_SELECTOR,'a.news_tit')
    title = a_tag.text
    href = a_tag.get_attribute('href')
    print(title, href)

time.sleep(10)










