class Player:
    def __init__(self, sailor, cannoneer, barterer, craftsman, region, credits):
        self.sailor = sailor
        self.cannoneer = cannoneer
        self.barterer = barterer
        self.craftsman = craftsman
        self.region = region
        self.credits = credits

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