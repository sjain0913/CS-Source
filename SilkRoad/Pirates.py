import random
import app, Player, Ship
class Pirates:

    success = True

    def __init__(self):
        self.success = Pirates.success
        self.credits = random.randint(1, 1000)
        item_list = app.player.inventory.keys()
        self.stolen_item = item_list[random.randint(0, len(item_list) - 1)]
        self.ransom = random.randint(100,250)
    
    def flee(self):
        chance_of_success = random.randint(30, 70) * (app.player.sailor / 3)
        if (chance_of_success >= 40):
            self.success = True
        else:
            self.success = False
            app.player.ship.health -= random.randint(25,50)
            if (app.player.credits < self.ransom):
                self.credits += app.player.credits
                app.player.credits = 0
                app.player.remove_from_inv(self.stolen_item)
            else:
                self.credits += self.ransom
                app.player.credits -= self.ransom
    
    def fight(self):
        chance_of_success = random.randint(30,70) * (app.player.cannoneer / 3)
        if (chance_of_success >= 60):
            self.success = True
            app.player.credits += self.credits
        else:
            self.success = False
            app.player.ship.health -= random.randint(25,50)
            if (app.player.credits <= self.ransom):
                self.credits += app.player.credits
                app.player.credits = 0
            else:
                self.credits += self.ransom
                app.player.credits -= self.ransom

    def pay(self):
        if (app.player.credits >= self.ransom):
            app.player.credits -= self.ransom
            self.credits += self.ransom
        elif (app.player.credits < self.ransom):
            app.player.inventory = []
        elif (app.player.inventory == [] and app.player.credits < self.ransom):
            app.player.ship.health -= random.randint(25,50)

