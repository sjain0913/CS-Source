import random
import Region, TechLevel
class Universe:
    __instance = None

    def __init__(self, regionList):
        if Universe.__instance != None:
            raise Exception("There is only one universe! (Maybe)")
        else:
            Universe.__instance = self
            self.regions = []
            for i in regionList:
                self.regions.append(Region.Region(i, TechLevel.TechLevel(random.randint(0,6)), random.randint(-200,200), random.randint(-200, 200)))

    @staticmethod
    def getInstance():
        return Universe.__instance