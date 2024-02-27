class TextGame:

    def __init__(self, player):
        self.turn = 1
        self.score = 0
        self.map = []
        self.player = player
        self.enemies = []

    def setup_board(self):
        for i in range(5):
            for j in range(i * i):
                self.map.append(i)

    def make_turn(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Turn {}".format(self.turn))
        self.player.take_turn(self)
        self.enemy_turn()

        if self.player.health <= 0:
            self.game_over()
        else:
            self.turn += 1
            self.make_turn()

    def game_over(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Game Over - Player " + str(self.player.name) + " is dead!")

    def enemy_turn(self):
        for i in self.enemies:
            self.enemies[i].take_turn(self)


class Character:

    def __init__(self, health, movement, name):
        self.name = ''
        self.health = 0
        self.movement = 0

    def defense(self):
        pass


class Player(Character):
    def __init__(self, health, movement, name, apl):
        super().__init__(health, movement, name)
        self.apl = apl

    def take_turn(self):
        ap_to_use = self.apl

        while ap_to_use > 0:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\nWhat do you want to do?\n1. Attack\n2. Shoot\n3. Heal\n4. Move\n")
            choice = input("\nEnter your choice(1,2,3,4): ")

            while choice not in ['1', '2', '3', '4']:
                choice = input("\nYou entered an invalid choice. Please choose one from 1,2,3,4: ")

            if choice == 1:
                self.attack()
            elif choice == 2:
                self.shoot()
            elif choice == 3:
                self.move()
            elif choice == 4:
                self.heal()

            ap_to_use -= 1

    def move(self):
        pass

    def attack(self, text_game):
        dead_enemies = []
        
        for enemy in range(len(text_game.enemies)):
            if text_game.enemies[enemy].distance <= 3:
                text_game.enemies[enemy].health -= 5
                if text_game.enemies[enemy].health <= 0:
                    dead_enemies.append(enemy)

        for enemy in dead_enemies:
            del text_game.enemies[enemy]

    def heal(self):
        print("\nHealing...")
        self.health = 20
        print("Health is " + str(self.health) + "\n")

    def shoot(self):
        pass


class Enemy(Character):
    def __init__(self, health, movement, name, damage, distance, speed):
        super().__init__(health, movement, name)
        self.damage = damage
        self.distance = distance
        self.speed = speed

    def move(self):
        pass

    def attack(self):
        pass

    def take_turn(self):
        pass


player = Player(20, 5, 'Hero')

game = TextGame(player)
game.setup_board()
