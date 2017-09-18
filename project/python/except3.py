import re

#pattern과 source를 생성자 매개변수로 갖는 Exception 클래스 정의
class NotMatchedException(Exception):
    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source
    #print(obj)했을 때 출력될 내용
    def __str__(self):
        return f'패턴 "{self.pattern}"을 "{self.source}"에서 찾지 못했습니다.'

#pattern과 source 매개변수를 받아 re.search 소스(source)에서 패턴(pattern)을 검색, 찾지 못하면 NotMatchedException이 발생

def search_from_source(pattern, source):
    m = re.search(pattern, source)
    if not m:
        raise NotMatchedException(pattern, source)
    return m

source_string = 'Lux, the Lady of Luminosity'
pattern1 = r'L\w{5}\b'
result = None

try:
    result = search_from_source(pattern1, source_string)
except NotMatchedException as e:
    print(e)

print('Search result:', result)
