import Universe

regionNames = ['China','India','Denmark','Great Britain','Egypt','Somalia','Persia','Java','Byzantium','Arabia']

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.regionNames= Game.regionNames

    def startGame(self):
        