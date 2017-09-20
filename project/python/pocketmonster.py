class Monster:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, target):
        return "{}가 {}를 공격해 {}의 피해를 입혔다!".format(self.name, target, self.damage)

    def __str__(self):
        return "{} : 공격력 {}".format(self.name, self.damage)


if __name__ == "__main__":
    pikachu = Monster('피카츄', '130')
    ggobugi = Monster('꼬부기', '100')
    print(pikachu)
    print(ggobugi)
    print(pikachu.attack(ggobugi))