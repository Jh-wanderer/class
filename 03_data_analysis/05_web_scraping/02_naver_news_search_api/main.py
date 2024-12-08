# 네이버 검색 API 예제 - 블로그 검색
# https://developers.naver.com/docs/serviceapi/search/blog/blog.md#python

import os
import sys
import urllib.request

# Web Rest API방식 호출
client_id = "AO07MQRJj4PjhIjyWH5x"
client_secret = "KE9zQxzE64"

# 검색어
encText = urllib.parse.quote("추천료칸")

# 요청 헤더 설정
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과, 문자열 통합, dict와 형식이 비슷함
#url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret) # 검색시 나오는 \는 그 뒤에 붙는 문자를 인식시키기 위한 표시

# 실제 요청 후 응답
response = urllib.request.urlopen(request)

# 응답코드 확인 : 200-성공, 4xx/5xx - 실패
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)