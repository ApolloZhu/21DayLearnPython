def transcript(x, y):
    return (abs(x), abs(y))

def printStat(message = "Status", start="", end="", prefix="--[__", suffix="__]--"):
    print(start + prefix + message + suffix + end)

class Ant:
    def __init__(self, name="Ant", x=0, y=0, color="black"):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        printStat("# New %s! #" % self.name, start="\n")
        self.describe()

    def attack(self):
        printStat("Attacking using mouth")

    def crawl(self, x, y):
        printStat("Crawling")
        self.move(x, y)
    def move(self, x, y):
        self.__updateLocation(*transcript(x, y))
        self.describe()
    def __updateLocation(self, x, y):
        self.x += x;
        self.y += y;
        
    def describe(self):
        print("Location of %s: (%d, %d)" % (self.name, self.x, self.y))

class FlyAnt(Ant):
    def attack(self):
        printStat("Attacking using pin")
    def fly(self, x, y):
        printStat("Flying")
        self.move(x, y)

class FinalAnt(FlyAnt):
    def attack(self):
        printStat("Attacking as a whole")
    def jump(self):
        printStat("Jumping")
