import random
import app, Player, Ship
class Navy:
    success = True

    def __init__(self, success):
        self.success = success
        self.item_list = app.player.inventory.keys()
        self.black_listed_item = app.player.item_list[random.randint(0,len(item_list) - 1)]

    def flee(self, success):
        chance_of_success = random.randint(30, 70) * (app.player.sailor / 3)
        if (chance_of_success >= 60):
            self.success = True
        else:
            self.success = False
            app.player.ship.health -= random.randint(25,50)
        
    def fight(self, success):
        chance_of_success = random.randint(30, 70) * (app.player.cannoneer / 3)
        if (chance_of_success >= 40):
            self.success = True
        else:
            self.success = False 
            app.player.remove_from_inv(black_listed_item)

    def forfeit(self, item_list):
        app.player.remove_from_inv(black_listed_item)

