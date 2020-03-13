class City:
    def __init__(self, lon, lat,name):
        self.lon = lon
        self.lat = lat
        self.name = name
    
    def distance(self, city):
        xDis = abs(self.lon - city.lon)
        yDis = abs(self.lat- city.lat)
        distance = (xDis ** 2) + (yDis ** 2)
        return distance
    
    def __repr__(self):
        # return f"name: {self.name}, lat: {self.lat}, lon: {self.lon}"
        return [self.name,self.lat,self.lon]
def CreateCitiesList(country):
    CityList = []
    for i in range(len(country)):
        CityList.append(City(country[i][1],country[i][2],country[i][0]))
    return CityList