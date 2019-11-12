import random
import app
import Player
import Ship
from Market import Market
class Trader:

    def __init__(self):
        self.market = Market("Trader")
        self.success = True

    def negotiate_prices(self):
        chance_of_success = random.randint(30, 70) * (app.player.merchant / 3)
        if chance_of_success >= 40:
            pass
        else:
            pass

    def rob(self):
        chance_of_success = random.randint(30, 70) * (app.player.cannoneer / 3)
        if chance_of_success >= 60:
            for i in self.market.items.keys():
                app.player.add_to_inv(i)
        else:
            app.player.ship.health -= 50

    def buy(self, item):
        self.market.buy(item)

    def sell(self, item):
        self.market.sell(item)
