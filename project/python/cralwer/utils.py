from urllib.parse import urlparse, parse_qs
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

# Episode namedtuple 정의
Episode = namedtuple('Episode', ['no', 'img_url', 'title', 'rating', 'created_date'])

def get_webtoon_episode_list(webtoon_id, page=1):
    webtoon_list_url = 'http://comic.naver.com/webtoon/list.nhn'
    params = {
            'titleId': webtoon_id,
            'page': page,
    }
    response = requests.get(webtoon_list_url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')

    episode_list = list()
    webtoon_table = soup.select_one('table.viewList')
    tr_list = webtoon_table.find_all('tr', recursive=False)
    # find_all은 직계 자손 안쪽까지 모두 탐색하지만, recursive=False를 하면 직계 자손만 탐색한다.
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) < 4:
            continue
        td_thumbnail = td_list[0]
        td_title = td_list[1]
        td_rating = td_list[2]
        td_created_date = td_list[3]

        url_episode = td_thumbnail.a.get('href')
        parse_result = urlparse(url_episode)
        queryset = parse_qs(parse_result.query)
        no = queryset['no'][0]

        img_url = td_thumbnail.a.img.get('src')
        title = td_title.get_text(strip=True)
        rating = td_rating.strong.get_text(strip=True)
        created_date = td_created_date.get_text(strip=True)

        episode = Episode(
            no=no,
            img_url=img_url,
            title=title,
            rating=rating,
            created_date=created_date
        )
        episode_list.append(episode)

    return episode_list
