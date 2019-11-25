import random
from Player import Player
import Ship
from Market import Market
class Trader:

    def __init__(self, player):
        self.market = Market("Trader")
        self.success = True
        self.player = player

    def negotiate_prices(self):
        chance_of_success = random.randint(30, 70) * (self.player.barterer / 3)
        if chance_of_success >= 40:
            pass
        else:
            pass

    def rob(self):
        chance_of_success = random.randint(30, 70) * (self.player.cannoneer / 3)
        if chance_of_success >= 60:
            for i in self.market.items.keys():
                self.player.add_to_inv(i)
        else:
            self.player.ship.health -= 50

    def buy(self, item):
        self.market.remove_from_market

    def sell(self, item):
        self.market.sell(item, self.player)

    def negotiate(self):
        print("for later")