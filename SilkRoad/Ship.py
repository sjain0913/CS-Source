class Ship:
    ships = ["Clipper", "Brig", "Battleship", "Galleon"]
    
    def __init__(self, ship_type):
        self.ship_type = ship_type
        if ship_type == Ship.ships[0]:
            self.cargo_space = 4
            self.fuel_cap = 10
            self.health = 200
        elif ship_type == Ship.ships[1]:
            self.cargo_space = 6
            self.fuel_cap = 15
            self.health = 350
        elif ship_type == Ship.ships[2]:
            self.cargo_space = 8
            self.fuel_cap = 20
            self.health = 500
        elif ship_type == Ship.ships[3]:
            self.cargo_space = 10
            self.fuel_cap = 25
            self.health = 650
        self.fuel = self.fuel_cap
    
    def ship_upgrade(self, ship_type, cargo_space, fuel_cap, health):
        self.ship_type = ship_type
        self.cargo_space = cargo_space
        self.fuel_cap = fuel_cap
        self.health = health

    def change_ship_type(self, ship_type):
        if ship_type == Ship.ships[1]:
            ship_upgrade(Ship.ships[1], 4, 10, 200)
        elif ship_type == Ship.ships[2]:
            ship_upgrade(Ship.ships[2], 6, 15, 350)
        elif ship_type == Ship.ships[3]:
            ship_upgrade(Ship.ships[3], 8, 20, 500)
        elif ship_type == Ship.ships[4]:
            ship_upgrade(Ship.ships[4], 10, 25, 650)