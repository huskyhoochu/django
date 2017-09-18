import re


f = open('sample.txt', 'rt')
source = f.read().strip()

#<td class="title">...</td>에 해당하는 내용들
p = re.compile(r'<td class="title".*?>.*?</td>', re.DOTALL)

result = re.findall(p, source)

for index, item in enumerate(result):
    print('=== index %s ===' % index)
    #>와 < 사이의 공백을 모두 없앰
    cur_strip_item = re.sub(r'>\s*?<',r'><', item, flags=re.DOTALL)
    #print(cur_strip_item)
    #a 태그 내부의 내용을 출력
    next_strip_item = re.sub(r'.*?<a.*?>(.*?)</a>.*',r'\g<1>',  cur_strip_item)
    print(next_strip_item)

print('Total items: ', len(result))
