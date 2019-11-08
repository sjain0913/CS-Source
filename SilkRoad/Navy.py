import random
import app, Player, Ship
class Navy:
    success = True

    def __init__(self, success):
        self.success = success
        self.black_listed_item = Player.inventory[random.randint(0, len(Player.inventory) - 1)]

    def flee(self, success):
        chance_of_success = random.randint(30, 70) * (app.player.sailor / 3)
        if (chance_of_success >= 60):
            Navy.success = True
        else:
            Navy.success = False
            Ship.health -= random.randint(25,50)
        
    def fight(self, success):
        chance_of_success = random.randint(30, 70) * (app.player.cannoneer / 3)
        if (chance_of_success >= 40):
            Navy.success = True
        else:
            Navy.success = False 
            Ship.health -= random.randint(25,50)
            Player.inventory.remove(black_listed_item)

    def forfeit(self, item_list):
        Player.inventory.remove(black_listed_item)
