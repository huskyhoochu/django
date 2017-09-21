import os
import requests
import pickle
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
import utils


class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()
        self.load(init=True)

    @property  # 프로퍼티 덕분에 속성값처럼 접근하게 되어서 ()를 안써도 호출 가능
    def total_episode_count(self):
        """
        webtoon_id에 해당하는 실제 웹툰의 총 episode 수를 리턴
        requests를 사용
        :return: 총 episode 수 (int)
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)

    @property 
    def up_to_date(self):
        """
        현재 가지고 있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        1. cur_episode_count = self.episode_list의 개수
        2. total_episode_count = 웹상의 총 episode 개수
        3. 위 두 변수의 값이 같으면 return True, 아니면 return False
        :return: boolean값
        """
        cur_episode_count = len(self.episode_list)
        total_episode_count = self.total_episode_count
        return cur_episode_count == total_episode_count

    def update_episode_list(self, force_update=False):
        """
        1. recent_episode_no=self.episode_list에서 가장 최신화의 no
        2. while문 또는 for문 내부에서 page값을 늘려가며
            utils.get_webtoon_episode_list를 호출
            반환된 list(episode)들을 해당 episode no가
            recent_episode_no보다 클 때까지만 self.episode_list에 추가
        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수 (int)
        """
        recent_episode_no = self.episode_list[0].no if self.episode_list else 0
        print('-update episode list start (Recent episode no: %s)-' % recent_episode_no)
        page = 1
        new_list = list()
        while True:
            print(' Get webtoon episode list (page %s)' % page)
            # 계속해서 증가하는 'page'를 이용해 다음 episode 리스트들을 가져옴
            el = utils.get_webtoon_episode_list(self.webtoon_id, page)
            for episode in el:
                # 각 episode의 no가 recent_episode_no보다 클 경우,
                # self.episode_list에 추가
                if int(episode.no) > int(recent_episode_no):
                    #최신화까지의 내용을 new_list에 넣는다
                    new_list.append(episode)
                    if int(episode.no) == 1:
                        break
                else:
                    break
            # break가 호출되지 않았을 때
            else:
                #계속해서 진행해야 하므로 page값을 증가시키고 continue로 처음으로 돌아감
                page += 1
                continue
            # el의 for문에서 break가 호출될 경우(더 이상 추가할 episode없음)
            # while문을 빠져나가기 위해 break 실행
            break
        #새 리스트를 기존의 리스트에 합친다
        self.episode_list = new_list + self.episode_list
        return f"{new_list[0].title}까지 업데이트 완료"

    def get_last_page_episode_list(self):
        """
        첫 번째 페이지의 내용만 가져오는 테스트 메소드
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id, 99999)
        self.episode_list = el
        return len(self.episode_list)

    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 저장

        1. 폴더 생성시
            os.is_ai(path)
            pa
        :return: None
        """
        # db폴더가 있는지 걱
        if not os.path.isdir('db'):
            os.mkdir('db')
        
        obj = self.episode_list
        path = 'db/%s.txt' % self.webtoon_id

        pickle.dump(obj, open(path, 'wb'))


    def load(self, path=None):
        """
        현재폴더를 기준으로 db/webtoon_id.txt 파일의 내용을 불러와
        pickle로 self.episode_list 복원
        """
        try:
            path = f'db/{self.webtoon_id}.txt'
            self.episode_list = pickle.load(open(path, 'rb'))
        except FileNotFoundError:
            if not init:
                print('파일이 없습니다.')


if __name__ == '__main__':
    webtoon_yumi = 651673
    webtoon_denma = 119874
    webtoon_blood = 696617
    nws = NaverWebtoonCrawler(webtoon_blood)
    print(nws.total_episode_count)
    print(nws.up_to_date)
    print(nws.get_last_page_episode_list())
    print(nws.update_episode_list())
    print(nws.save())
    print(nws.load())