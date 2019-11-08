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
            Pirates.success = True
        else:
            Pirates.success = False
            Ship.health -= random.randint(25,50)
            if (app.player.credits < Pirates.ransom):
                Pirates.credits += app.player.credits
                app.player.credits = 0
                Player.inventory.remove(Pirates.stolen_items)
            else:
                Pirates.credits += Pirates.ransom
                app.player.credits -= Pirates.ransom
    
    def fight(self):
        chance_of_success = random.randint(30,70) * (app.player.cannoneer / 3)
        if (chance_of_success >= 60):
            Pirates.success = True
            app.player.credits += Pirates.credits
        else:
            Pirates.success = False
            Ship.health -= random.randint(25,50)
            if (app.player.credits <= Pirates.ransom):
                Pirates.credits += app.player.credits
                app.player.credits = 0
            else:
                Pirates.credits += Pirates.ransom
                app.player.credits -= Pirates.ransom

    def pay(self):
        if (app.player.credit >= Pirates.ransom):
            app.player.credit -= Pirates.ransom
            Pirates.credits += Pirates.ransom
        elif (app.player.credit < Pirates.ransom):
            Player.inventory = []
        elif (Player.inventory == [] and app.player.credit < Pirates.ransom):
            Ship.health -= random.randint(25,50)

