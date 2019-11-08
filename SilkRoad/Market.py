from Item import Item
import app, random
class Market:
    def __init__(self, tech_level):
        self.items = {}
        temp = []
        if tech_level is "STONE_AGE":
            temp = Item.stone_items
        elif tech_level is "BRONZE_AGE":
            temp = Item.bronze_items
        elif tech_level is "IRON_AGE":
            temp = Item.iron_items
        elif tech_level is "EARLY_MIDDLE_AGES":
            temp = Item.early_middle_items
        elif tech_level is "LATE_MIDDLE_AGES":
            temp = Item.late_middle_items
        elif tech_level is "EARLY_MODERN":
            temp = Item.early_modern_items
        elif tech_level is "MODERN":
            temp = Item.modern_items
        else:
            temp = Item.trader_items
        price_mult = 3 / app.player.barterer
        for i in temp:
            self.items[i] = Item(i, price_mult, random.randint(0,10))

    def buy(self, item):
        to_buy = self.items[item]
        app.player.credits = app.player.credits - to_buy.value
        app.player.add_to_inv(item)
        if (to_buy.number > 1):
            to_buy.dec_number()
        else:
            self.items[item] = None

    def sell(self, item):
        to_sell = app.player.inventory[item]
        app.player.credits = app.player.credits + to_sell.value
        app.player.remove_from_inv(item)
