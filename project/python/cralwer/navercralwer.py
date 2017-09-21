import requests

from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
from utils import Episode

# NamedTuple(Episode)를 사용해서
#   이미지 주소(img_url)
#   에피소드 제목(title)
#   에피소드 별점(rating)
#   에피소드 등록일(created_date)
# 를 가지는 NamedTuple의 리스트를 생성

# webtoon id를 입력받아 해당 웹툰의 첫 번째 페이지에 있는 episode 리스트를 리턴하는 함수 구현
# request를 사용

webtoon_yumi = 651673
webtoon_denma = 119874

def save_episode_list_to_file(webtoon_id, episode_list):
    """
    episode_list로 전달된 Episode의 리스트를
    쉼표단위로 속성을 구분, 라인단위로 episode를 구분해 저장
    파일명은 <webtoon_id>_<가장 최근 에피소드no>_<가장 나중 에피소드no>.txt
    """
    filename = '{webtoon_id}_{first_episode_no}_{last_episode_no}.txt'.format(
        webtoon_id=webtoon_id,
        # episode_list의 0번째 Episode의 no 속성
        first_episode_no=episode_list[0].no,
        # episode_list의 마지막 Episode의 no 속성
        last_episode_no=episode_list[-1].no,
    )
    # 위에서 작성한 <webtoon_id>_<first_episode_no>_<last_episode_no>.txt 파일에 작성
    with open(filename, 'wt') as f:
        # 각 episode를 순회하며 각 line에 해당하는 문자열을 생성, 기록
        for episode in episode_list:
            f.write('|'.join(episode) + '\n')

def load_episode_list_from_file(path):
    """
    path에 해당하는 file을 읽어 Episode 리스트를 생성해 리턴
    """

    with open(path, 'rt') as f:
        return [Episode._make(line.strip().split('|')) for line in f]

def get_webtoon_episode_list(webtoon_id, page=1):
    """
    특정 page의 episode 리스트를 리턴하도록 리팩토링
    :param webtoon_id: 웹툰 고유 ID
    :param page: 가져오려는 Episode list 페이지
    :return: list(Episode)
    """
    # webtoon_url을 기반으로 특정 웹툰의 리스트 페이지 내용을 가져와 soup객체에 할당
    webtoon_list_url = 'http://comic.naver.com/webtoon/list.nhn'
    params = {
        'titleId': webtoon_id,
        'page': page,
    }
    response = requests.get(webtoon_list_url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')

    episode_list = list()
    webtoon_table = soup.select_one('table.viewList')
    tr_list = webtoon_table.find_all('tr', recursive=false)
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) < 4:
            continue
        td_thumbnail = td_list[0]
        td_title = td_list[1]
        td_rating = td_list[2]
        td_created_date = td_list[3]

        # Episode 고유의 no
        url_episode = td_thumbnail.a.get('href')
        parse_result = urlparse(url_episode)
        queryset = parse_qs(parse_result.query)
        no = queryset['no'][0]
        img_url = td_thumbnail.a.img.get('src')
        title = td_title.get_text(strip=True)
        rating = td_rating.strong.get_text(strip=True)

        episode = Episode(
            no=no,
            img_url=img_url,
            title=title,
            rating=rating,
            created_date=created_date,
        )
        episode_list.append(episode)

    return episode_list
