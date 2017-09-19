import utils

class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()

    @property
    def total_episode_count(self):
        '''
        webtoon_id에 해당하는 실제 웹툰의 총 episode 수를 리턴
        requests를 사용
        '''
        utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)

    def get_episode_list(self, page=1):
        el = utils.get_webtoon_episode_list(self.webtoon_id, page)
        self.episode_list.extend(el)

    def clear_episode_list(self):
        pass

    def get_all_episode_list(self):
        pass

    def add_new_episode_list(self):
        pass


if __name__ == "__main__":
    nwc = NaverWebtoonCrawler(651673)
    print(nwc.total_episode_count())