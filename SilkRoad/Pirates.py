import random
import Player
import Ship
class Pirates:

    success = True

    def __init__(self, player):
        self.success = Pirates.success
        self.credits = random.randint(1, 1000)
        item_list = player.inventory.keys()
        self.player = player
        self.stolen_item = item_list[random.randint(0, len(item_list) - 1)]
        self.ransom = random.randint(100, 250)
    
    def flee(self):
        chance_of_success = random.randint(30, 70) * (self.player.sailor / 3)
        if chance_of_success >= 40:
            self.success = True
        else:
            self.success = False
            self.player.ship.health -= random.randint(25, 50)
            if self.player.credits < self.ransom:
                self.credits += self.player.credits
                self.player.credits = 0
                self.player.remove_from_inv(self.stolen_item)
            else:
                self.credits += self.ransom
                self.player.credits -= self.ransom
    
    def fight(self):
        chance_of_success = random.randint(30, 70) * (self.player.cannoneer / 3)
        if chance_of_success >= 60:
            self.success = True
            self.player.credits += self.credits
        else:
            self.success = False
            self.player.ship.health -= random.randint(25, 50)
            if self.player.credits <= self.ransom:
                self.credits += self.player.credits
                self.player.credits = 0
            else:
                self.credits += self.ransom
                self.player.credits -= self.ransom

    def pay(self):
        if self.player.credits >= self.ransom:
            self.player.credits -= self.ransom
            self.credits += self.ransom
        elif self.player.credits < self.ransom:
            self.player.inventory = []
        elif self.player.inventory == [] and self.player.credits < self.ransom:
            self.player.ship.health -= random.randint(25, 50)
