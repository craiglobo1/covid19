from Population import initialPopulation, nextGeneration
from Fitness import rankRoutes
import matplotlib.pyplot as plt
from math import radians,sin,cos,atan2,sqrt

def distance(lat1,lon1,lat2,lon2):
		lat1 = radians(lat1)
		lon1 = radians(lon1)
		lat2 = radians(lat2)
		lon2 = radians(lon2)
		# approximate radius of earth in km
		R = 6373.0
		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance = R * c
		return distance


def setup(countries):
    plt.ion()
    fig = plt.figure()
    plt.title('Scatter Plot', fontsize=20)
    plt.xlabel('longitude', fontsize=15)
    plt.ylabel('latidude', fontsize=15)
    plt.show()
    return fig


def draw(countries,fig,string):
    plt.cla()
    countries = [[countries[i].name,countries[i].lon,countries[i].lat] for i in range(len(countries))]
    labels,xs,ys = zip(*countries)
    plt.plot(xs, ys, marker = 'o')
    for label, x, y in zip(labels, xs, ys):
        plt.annotate(label, xy = (x, y))
    plt.text(-10,-36,string)
    fig.canvas.draw()
    plt.pause(0.00000000000001)


def geneticAlgorithm(population, popSize, elitePercent, mutationRate, generations):
    eliteSize = int(round(elitePercent*popSize))
    pop = initialPopulation(popSize,population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


def LiveGeneticAlgorithm(population, popSize, elitePercent, mutationRate, generations):
    eliteSize = int(round(elitePercent*popSize))
    pop = initialPopulation(popSize, population)
    fig = setup(pop[0])
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        draw(pop[rankRoutes(pop)[0][0]], fig,f'Generations: {i+1}/{generations}')
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute
        

def geneticAlgorithmPlot(population, popSize, elitePercent, mutationRate, generations):
    eliteSize = int(round(elitePercent*popSize))
    pop = initialPopulation(popSize, population)
    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])
    
    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute