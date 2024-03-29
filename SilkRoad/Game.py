from Universe import Universe
from Player import Player
from Region import Region
from Ship import Ship
import app
import random


class Game:
    def __init__(self, difficulty, regions):
        self.difficulty = difficulty
        self.regions = regions

    def start_game(self):
        newUniverse = Universe(self.regions)
        regionNum = random.randint(0,9)
        player = app.player
        player.ship = Ship("Clipper")
        player.region = Universe.get_instance().regions[regionNum]
        if (self.difficulty is 'easy'):
            player.credits = 1000
        elif (self.difficulty is 'medium'):
            player.credits = 500
        else:
            player.credits = 100

    def get_difficulty(self):
        return self.difficulty
