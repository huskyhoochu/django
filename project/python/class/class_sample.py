class Shop:
    description = 'Python Shop Class'
    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address

    def show_name(self):
        print(self.name)

    def _get_show_info_text(self):
        return f'''상점 ({self.name})
         유형: {self._shop_type}
         주소: {self.address}'''

    def show_info(self):
        print(self._get_show_info_text())

    def change_type(self, new_type):
        if new_type not in ['패스트푸드', 'PC방']:
            print('해당 상점유형은 사용할 수 없습니다.')
        else:
            self._shop_type = new_type
            print('변경되었습니다.')

    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, new_type):
        if new_type not in ['패스트푸드', 'PC방']:
            print('해당 상점유형은 사용할 수 없습니다.')

        else:
            self._shop_type = new_type
            print('변경되었습니다.')

    def show_object_log(self, obj):
        print(obj.log)

class Restaurant(Shop):
    def __init__(self, name, shop_type, address, rating=5.0):
        super().__init__(name, shop_type, address)
        self.rating = rating

    def _get_show_info_text(self):
        ori = super()._get_show_info_text()
        ret = ori.replace('상점', '식당')
        print(ret)

    def show_info(self):
        print(self._get_show_info_text())

    @classmethod
    def make_dummy(cls):
        return Shop('untitled', 'undefined', 'unknown')




