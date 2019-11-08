import random
import app, Player, Ship
class Pirates:

    success = True

    def __init__(self):
        self.success = success
        self.credits = random.randint(1, 1000)
        self.stolen_item = Player.inventory[random.randint(0, len(Player.inventory) - 1)]
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
                app.player.inventory.remove(self.stolen_items)
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
        if (app.player.credit >= self.ransom):
            app.player.credit -= self.ransom
            self.credits += self.ransom
        elif (app.player.credit < self.ransom):
            app.player.inventory = []
        elif (app.player.inventory == [] and app.player.credit < self.ransom):
            app.player.ship.health -= random.randint(25,50)

