import random
from Item import Item
import app
from Game import Game

class Player:
    def __init__(self, name):
        self.name = name
        self.sailor = 0
        self.cannoneer = 0
        self.barterer = 0
        self.craftsman = 0
        self.region = None
        self.credits = credits
        self.ship = None
        self.inventory = {}
        self.game = Game

    def add_to_inv(self, item):
        if self.inventory[item] is not None:
            self.inventory[item].inc_number()
        else:
            self.inventory[item] = Item(item, (app.player.barterer / 3), 1)

    def remove_from_inv(self, item):
        if self.inventory[item] > 1:
            self.inventory[item].dec_number()
        else:
            self.inventory[item] = None

    def travel(self, region):
        trav = {}
        trav['toRegion'] = region
        if game.getDifficulty() == 1:
            if random.randint(0, 9) == 0:
                trav['enc'] = "Trader"
            elif random.randint(0, 3) == 0:
                trav['enc'] = "Pirate"
            elif random.randint(0, 2) == 0:
                trav['enc'] = "Navy"
            else:
                app.player.ship.fuel = app.player.ship.fuel - app.player.region.get_fuel_cost(
                    region.getX(), region.getY())
                app.player.region = region
        if game.getDifficulty() == 2:
            if random.randint(0, 6) == 0:
                trav['enc'] = "Trader"
            elif random.randint(0, 5) == 0:
                trav['enc'] = "Pirate"
            elif random.randint(0, 3) == 0:
                trav['enc'] = "Navy"
            else:
                app.player.ship.fuel = app.player.ship.fuel - app.player.region.get_fuel_cost(
                    region.getX(), region.getY())
                app.player.region = region
        if game.getDifficulty() == 3:
            if random.randint(0, 3) == 0:
                trav['enc'] = "Trader"
            elif random.randint(0, 7) == 0:
                trav['enc'] = "Pirate"
            elif random.randint(0, 4) == 0:
                trav['enc'] = "Navy"
            else:
                app.player.ship.fuel = app.player.ship.fuel - app.player.region.get_fuel_cost(
                    region.getX(), region.getY())
                app.player.region = region
        return trav

    def set_sailor(self, sailor):
        self.sailor = sailor

    def set_cannoneer(self, cannoneer):
        self.cannoneer = cannoneer

    def set_barterer(self, barterer):
        self.barterer = barterer

    def set_craftsman(self, craftsman):
        self.craftsman = craftsman

    def set_region(self, region):
        self.region = region

    def set_credits(self, credits):
        self.credits = credits

    def get_name(self):
        return self.name

    def get_sailor(self):
        return self.sailor

    def get_cannoneer(self):
        return self.cannoneer

    def get_barterer(self):
        return self.barterer

    def get_craftsman(self):
        return self.craftsman

    def get_region(self):
        return self.region

    def get_credits(self):
        return self.credits

    def increment_sailor(self):
        self.sailor += 1

    def increment_cannoneer(self):
        self.cannoneer += 1

    def increment_barterer(self):
        self.barterer += 1

    def increment_craftsman(self):
        self.craftsman += 1

    def decrement_sailor(self):
        self.sailor -= 1

    def decrement_cannoneer(self):
        self.cannoneer -= 1

    def decrement_barterer(self):
        self.barterer -= 1

    def decrement_craftsman(self):
        self.craftsman -= 1

    def setGame(self, Game):
        self.game = Game
