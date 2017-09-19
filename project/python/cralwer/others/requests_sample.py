import requests
from bs4 import BeautifulSoup

webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId=651673'

response = requests.get(webtoon_url)
source = response.text
soup = BeautifulSoup(source)
with open('sample.txt', 'wt') as f:
    f.write(soup.prettify())
print("덮어쓰기가 완료되었습니다.")

