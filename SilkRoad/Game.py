import Universe

regionNames = ['China','India','Denmark','Great Britain','Egypt','Somalia','Persia','Java','Byzantium','Arabia']

class Game:
    def __init__(self, difficulty, regionNames):
        self.difficulty = difficulty
        self.regionNames=regionNames

    def startGame(self):
        