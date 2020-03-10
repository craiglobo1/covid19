from random import sample,random,randint
from math import sin, cos, sqrt, atan2, radians, pow
def InitialPopulation(order,popSize):
    population = []
    for i in range(popSize):
        population.append(sample(order,len(order)))
    return population
def NextPopulation(population,fitness,MutationRate):
	NewPopulation = []
	for i in range(len(population)):
		order = PickOne(population,fitness)
		if round(MutationRate*len(population))%(i+1) == 0:
			mutate(order)
		NewPopulation.append(order) 
	return NewPopulation
def RelativeDist(lat1,lon1,lat2,lon2):
	dist = pow((lon2-lon1),2)+pow((lat2-lat1),2)
	return dist
def RelativeTotalDist(order):
    sum = 0
    for i in range(len(order)-1):
        sum += RelativeDist(order[i][1],order[i][2],order[i+1][1],order[i+1][2])
    return sum
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
def TotalDist(order):
    sum = 0
    for i in range(len(order)-1):
        sum += distance(order[i][1],order[i][2],order[i+1][1],order[i+1][2])
    return sum
def fitness(population,BestEverDist,BestEverExist=None):
	bestDist = RelativeTotalDist(population[0])
	BestEver = population[0]
	fitness=[]
	for order in population:
		d = RelativeTotalDist(order)
		if d < bestDist:
			bestDist= d
			BestEver = order
		fitness.append(1/d)
	fitnessNormalized = [order/sum(fitness) for order in fitness]
	if bestDist < BestEverDist:
		BestEver = BestEverExist
		bestDist = BestEverDist
	
	return BestEver,bestDist,fitnessNormalized
def PickOne(lists,prob):
	index = 0
	r = random()
	while r > 0:
		r-=prob[index]
		index+=1
	index-=1
	return lists[index]
def mutate(order):
	indexA = randint(0,len(order)-1)
	indexB = randint(0,len(order)-1)
	order[indexA],order[indexB] = order[indexB],order[indexA]