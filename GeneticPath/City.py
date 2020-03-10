class City:
    def __init__(self, x, y,name):
        self.x = x
        self.y = y
        self.name = name
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = (xDis ** 2) + (yDis ** 2)
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
def CreateCitiesList(country):
    CityList = []
    for i in range(len(country)):
        CityList.append(City(country[1],country[2],country[0]))
    return CityList