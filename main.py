class TextGame:

    def __init__(self):
        self.turn = 1
        self.score = 0
        self.map = 0
        self.player = 0
        self.enemies = []

    def setup_board(self):
        pass

    def make_turn(self):
        pass

    def game_over(self):
        pass


class Character:

    def __init__(self, health, movement, name):
        self.name = ''
        self.health = 0
        self.movement = 0

    def defense(self):
        pass

    def take_turn(self):
        pass


class Player(Character):
    def __init__(self, mana, health, movement, name):
        super().__init__(health, movement, name)
        self.mana = mana

    def move(self):
        pass

    def attack(self):
        pass

    def use_item(self):
        pass

    def use_ability(self):
        pass

    def shoot(self):
        pass


class Enemy(Character):
    def __init__(self, mana, health, movement, name, damage):
        super().__init__(health, movement, name)
        self.damage = damage

    def move(self):
        pass

    def attack(self):
        pass


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def use(self):
        pass


class weapon:
    def __init__(self,damage)