from TechLevel import TechLevel
from Market import Market
import math
class Region:
    def __init__(self, name, TechLevel, x, y):
        self.__techLevel = TechLevel
        self.__x = x
        self.__y = y
        self.__name = name
        self.market = Market(TechLevel)

    def get_fuel_cost(self, x, y, player):
        print(x)
        print(y)
        print(self.__x)
        print(self.__y)
        return (3 * math.sqrt((x-self.__x) * (x-self.__x) +
                              (y-self.__y) * (y-self.__y))) / (28 * player.get_sailor())

    def price_multiplier(self, player):
        if self.__techLevel == TechLevel(0):
            return 0.5 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(1):
            return 0.75 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(2):
            return 1.0 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(3):
            return 1.25 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(4):
            return 1.5 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(5):
            return 1.75 * 10.0/(player.barterer)
        elif self.__techLevel == TechLevel(6):
            return 2.0 * 10.0/(player.barterer)

    def getX(self):
        return self.__x

    def get_name(self):
        return self.__name

    def getY(self):
        return self.__y

    def getTechLevel(self):
        return self.__techLevel
