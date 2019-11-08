from Item import Item
import app, random
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
        if random.randint(0,9) == 0:
            trav['enc'] = "Trader"
            return trav
        elif random.randint(0,3) == 0:
            trav['enc'] = "Pirate"
            return trav
        elif random.randint(0,2) == 0:
            trav['enc'] = "Navy"
            return trav
        else:
            app.player.ship.fuel = app.player.ship.fuel - app.player.region.get_fuel_cost(
                region.getX(), region.getY())
            app.player.region = region
            return trav
    
    #Setters
    def setSailor(self, sailor):
        self.sailor = sailor

    def setCannoneer(self, cannoneer):
        self.cannoneer = cannoneer

    def setBarterer(self, barterer):
        self.barterer = barterer

    def setCraftsman(self, craftsman):
        self.craftsman = craftsman

    def setRegion(self, region):
        self.region = region

    def setCredits(self, credits):
        self.credits = credits

    #Getters
    def getName(self):
        return self.name

    def getSailor(self):
        return self.sailor

    def getCannoneer(self):
        return self.cannoneer

    def getBarterer(self):
        return self.barterer

    def getCraftsman(self):
        return self.craftsman

    def getRegion(self):
        return self.region

    def getCredits(self):
        return self.credits

    #Incrementing Stats
    def incrementSailor(self):
        self.sailor += 1

    def incrementCannoneer(self):
        self.cannoneer += 1

    def incrementBarterer(self):
        self.barterer += 1

    def incrementCraftsman(self):
        self.craftsman += 1

    #Decrementing Stats
    def decrementSailor(self):
        self.sailor -= 1

    def decrementCannoneer(self):
        self.cannoneer -= 1

    def decrementBarterer(self):
        self.barterer -= 1

    def decrementCraftsman(self):
        self.craftsman -= 1

