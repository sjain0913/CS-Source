from Item import Item
import random
class Market:
    def __init__(self, tech_level):
        self.items = {}
        self.price_mult = 1
        self.tech_level = tech_level

    def buy(self, item, player):
        to_buy = self.items[item]
        player.credits = player.credits - to_buy.value
        player.add_to_inv(item)
        if (to_buy.number > 1):
            to_buy.dec_number()
        else:
            self.items[item] = None

    def sell(self, item, player):
        to_sell = player.inventory[item]
        player.credits = player.credits + to_sell.value
        player.remove_from_inv(item)

    def add_to_market(self, item):
        if self.items[item] is not None:
            self.items[item].inc_number()
        else:
            self.items[item] = Item(item, self.price_mult, 1)

    def remove_from_market(self, item):
        self.items[item].dec_number()
        if self.items[item].number == 0:
            del(self.items[item])
    
    def populate_market(self, player):
        self.price_mult = 3 / player.barterer
        temp = []
        if self.tech_level is "STONE_AGE":
            temp = Item.stone_items
        elif self.tech_level is "BRONZE_AGE":
            temp = Item.bronze_items
        elif self.tech_level is "IRON_AGE":
            temp = Item.iron_items
        elif self.tech_level is "EARLY_MIDDLE_AGES":
            temp = Item.early_middle_items
        elif self.tech_level is "LATE_MIDDLE_AGES":
            temp = Item.late_middle_items
        elif self.tech_level is "EARLY_MODERN":
            temp = Item.early_modern_items
        elif self.tech_level is "MODERN":
            temp = Item.modern_items
        else:
            temp = Item.trader_items
        for i in temp:
            self.items[i] = Item(i, self.price_mult, random.randint(1,10))
        return self.items
