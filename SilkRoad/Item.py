class Item:
    stone_items = ["Ivory", "Animal Hide", "Meat"]
    bronze_items = ["Dye", "Lumber", "Wine"]
    iron_items = ["Cloth", "Iron", "Jewelry"]
    early_middle_items = ["Copper", "Gold", "Honey"]
    late_middle_items = ["Brass", "Gunpowder", "Silk"]
    early_modern_items = ["Coffee", "Paper", "Opium"]
    modern_items = ["Oil", "Rubber", "Textile"]
    trader_items = ["Ivory", "Animal Hide", "Meat",
                    "Dye", "Lumber", "Wine",
                    "Cloth", "Iron", "Jewelry",
                    "Copper", "Gold", "Honey",
                    "Brass", "Gunpowder", "Silk",
                    "Coffee", "Paper", "Opium",
                    "Oil", "Rubber", "Textile", "Golden Goose"]
    base_values = {"Ivory" : 6, "Animal Hide" : 2, "Meat" : 1,
                   "Dye" : 7, "Lumber" : 4, "Wine" : 9,
                   "Cloth" : 4, "Iron" : 5, "Jewelry" : 12,
                   "Copper" : 4, "Gold" : 10, "Honey" : 6,
                   "Brass" : 8, "Gunpowder" : 9, "Silk" : 13,
                   "Coffee" : 7, "Paper" : 5, "Opium" : 10,
                   "Oil" : 12, "Rubber" : 6, "Textile" : 7,
                   "Golden Goose" : 50}

    def __init__(self, name, price_mult, number):
        self.name = name
        self.buy_value = price_mult * Item.base_values[name]
        self.sell_value = Item.base_values / price_mult
        self.number = number

    def dec_number(self):
        self.number = self.number - 1

    def inc_number(self):
        self.number = self.number + 1
