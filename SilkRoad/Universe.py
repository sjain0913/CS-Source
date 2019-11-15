import random
import Region
import TechLevel
class Universe:
    __instance = None
    items = ["item 1", "item 2", "item 3", "item 4", "item 5",
             "item 6", "item 7", "item 8", "item 9", "item 10"]

    def __init__(self, regionList):
        if Universe.__instance != None:
            raise Exception("There is only one universe! (Maybe)")
        Universe.__instance = self
        self.regions = []
        for i in regionList:
            self.regions.append(Region.Region(i, TechLevel.TechLevel(random.randint(0, 6)).name,
                                              random.randint(-200, 200),
                                              random.randint(-200, 200)))

    @staticmethod
    def get_instance():
        return Universe.__instance
