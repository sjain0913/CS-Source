import random
from Item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.sailor = 0
        self.cannoneer = 0
        self.barterer = 0
        self.craftsman = 0
        self.karma = 0
        self.region = None
        self.credits = credits
        self.ship = None
        self.inventory = {}

    def add_to_inv(self, item):
        if self.inventory[item] is not None:
            self.inventory[item].inc_number()
        else:
            self.inventory[item] = Item(item, (self.barterer / 3), 1)

    def remove_from_inv(self, item):
        if self.inventory[item] > 1:
            self.inventory[item].dec_number()
        else:
            del(self.inventory[item])

    def travel(self, region, game):
        trav = {}
        trav['toRegion'] = region
        if self.game.getDifficulty() == 1:
            chance = random.randint(0,15+self.karma)
            if chance in [0,1,2,3,4]:
                trav['enc'] = "Trader"
            elif chance in [5,6]:
                trav['enc'] = "Pirate"
            elif chance in [7,8,9]:
                trav['enc'] = "Navy"
            else:
                self.ship.fuel = self.ship.fuel - self.region.get_fuel_cost(
                    region.getX(), region.getY(), self)
                self.region = region
        if self.game.getDifficulty() == 2:
            chacne = random.randint(0,15+self.karma)
            if chacne in [0,1,2]:
                trav['enc'] = "Trader"
            elif chacne in [3,4,5]:
                trav['enc'] = "Pirate"
            elif chacne in [6,7,8,9]:
                trav['enc'] = "Navy"
            else:
                self.ship.fuel = self.ship.fuel - self.region.get_fuel_cost(
                    region.getX(), region.getY(), self)
                self.region = region
        if self.game.getDifficulty() == 3:
            chance = random.randint(0,15+self.karma)
            if chance in [0]:
                trav['enc'] = "Trader"
            elif chance in [1,2,3,4]:
                trav['enc'] = "Pirate"
            elif chance in [5,6,7,8,9]:
                trav['enc'] = "Navy"
            else:
                self.ship.fuel = self.ship.fuel - self.region.get_fuel_cost(
                    region.getX(), region.getY(), self)
                self.region = region
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

    def set_game(self, game):
        self.game = game
