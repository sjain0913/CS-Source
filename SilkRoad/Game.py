from Universe import Universe
import Player
from Region import Region
from Ship import Ship
import app
import random


class Game:
    def __init__(self, difficulty, regions):
        self.difficulty = difficulty
        self.regions = regions

    def startGame(self):
        newUniverse = Universe(self.regions)
        regionNum = random.randint(0,9)
        player = app.player
        player.ship = Ship("Clipper")
        player.region = Universe.getInstance().regions[regionNum]
        if (self.difficulty is 'easy'):
            player.credits = 1000
        elif (self.difficulty is 'medium'):
            player.credits = 500
        else:
            player.credits = 100

    def getDifficulty(self):
        return self.difficulty
