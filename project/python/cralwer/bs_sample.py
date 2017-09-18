from bs4 import BeautifulSoup

f = open('sample.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'lxml')

result_list = soup.find_all("td", attrs = {"class":"title"})
for index, item in enumerate(result_list):
    print('=== index %s ===' % index)
    strip_item = item.a.text
    print(strip_item)
