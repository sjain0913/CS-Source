class Region: 
    def __init__(self, name, techLevel, x, y):
        self.__techLevel = techLevel
        self.__x = x
        self.__y = y
        self.__name = name

    def getX(self):
        return self.__x

    def getName(self):
        return self.__name

    def getY(self):
        return self.__y

    def getTechLevel(self):
        return self.__techLevel
