from collections import namedtuple
from urllib.parse import urlparse, parse_qs
import requests
import pickle
from bs4 import BeautifulSoup

Episode = namedtuple('Episode', ['no', 'img_url', 'title', 'rating', 'created_date'])

webtoon_yumi = 651673
webtoon_denma = 119874

def save_episode_list_to_file(webtoon_id, episode_list):
    filename = ('<{}>_<{}>_<{}>.txt'.format(webtoon_id, episode_list[0].no, episode_list[-1].no))

    with open(filename, 'wt') as f:
        for episode in episode_list:
            f.write(','.join(episode) + '\n')

    print("쓰기 완료")

def load_episode_list_from_file(path):
    episode_list = list()
    with open(path, 'rt') as f:
        return print([Episode._make(line.strip().split(',')) for line in f])
    #     for line in f:
    #         episode = Episode._make(line.strip().split(','))
    #         episode_list.append(episode)
    # return episode_list
        # while True:
        #     line = f.readline()
        #     if not line:
        #         break
        #     output.append(line)
    #
    # return print(output)




def webtoon_parser(webtoon_id):
    webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId={}'.format(webtoon_id)

    response = requests.get(webtoon_url)
    source = response.text
    soup = BeautifulSoup(source, 'lxml')

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
            no = no,
            img_url = img_url,
            title = title,
            rating = rating,
            created_date = created_date
        )
        episode_list.append(episode)

    return episode_list


li = webtoon_parser(webtoon_denma)

pickle.dump(li, open('denma_pickle.txt', 'wb'))

# save_episode_list_to_file(webtoon_denma, li)
# load_episode_list_from_file('<119874>_<1060>_<1051>.txt')