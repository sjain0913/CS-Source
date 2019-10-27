from Universe import Universe
from Player import Player
from Region import Region
from Ship import Ship
import app
import random

regionNames = ['China','India','Denmark','Britain','Egypt','Somalia','Persia','Java','Byzantium','Arabia']

class Game:
    def __init__(self, difficulty, regions):
        self.difficulty = difficulty
        self.regions = regions

    def startGame(self):
        newUniverse = Universe(regionNames)
        regionNum = random.randint(0,9)
        player = app.player
        player.ship = Ship("Clipper")
        player.setRegion(Universe.getInstance().regions[regionNum])
        if (self.difficulty is 'easy'):
            player.setCredits(1000)
        elif (self.difficulty is 'medium'):
            player.setCredits(500)
        else:
            player.setCredits(100)

    def getDifficulty(self):
        return self.difficulty
