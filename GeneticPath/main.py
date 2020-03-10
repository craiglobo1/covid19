import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle
from pop_fit import InitialPopulation, PickOne, NextPopulation, TotalDist , RelativeTotalDist
countries =[['Algeria', 2.9999825, 28.0000272], ['Nigeria', 7.9999721, 9.6000359], ['Senegal', -14.4529612, 14.4750607],
['South Africa', 24.991639, -28.8166236], ['Americas', -99.5486812, 19.1982908], ['Argentina', -64.9672817, -34.9964963],
['Brazil', -53.2, -10.3333333]]
# countries = [['Algeria', 2.9999825, 28.0000272], ['Nigeria', 7.9999721, 9.6000359], ['Senegal', -14.4529612, 14.4750607],
# ['South Africa', 24.991639, -28.8166236], ['Americas', -99.5486812, 19.1982908], ['Argentina', -64.9672817, -34.9964963],
# ['Brazil', -53.2, -10.3333333], ['Canada', -107.9917071, 61.0666922],['Chile', -71.3187697, -31.7613365],
# ['Dominican Republic', -70.3028026, 19.0974031], ['Ecuador', -79.3666965, -1.3397668], ['Guadalupe', -97.8279576, 29.6480061],
# ['Mexico', -99.1331785, 19.4326296], ['United States', -100.4458825, 39.7837304], ['Afghanistan', 66.2385139, 33.7680065],
# ['Bahrain', 50.5344606, 26.1551249], ['Egypt', 29.2675469, 26.2540493], ['Iran', 54.5643516, 32.6475314],
# ['Iraq', 44.1749775, 33.0955793], ['Jordan', 36.941628, 31.1667049], ['Kuwait', 47.4979476, 29.2733964],
# ['Lebanon', 35.843409, 33.8750629], ['Morocco', -7.3362482, 31.1728205], ['Oman', 57.0036901, 21.0000287],
# ['Pakistan', 71.247499, 30.3308401], ['Qatar', 51.2295295, 25.3336984], ['Saudi Arabia', 42.3528328, 25.6242618],
# ['Tunisia', 9.400138, 33.8439408], ['United Arab Emirates', 53.9994829, 24.0002488], ['Andorra', 1.5732033, 42.5407167],
# ['Armenia', 44.6736646, 40.7696272], ['Austria', 13.199959, 47.2000338], ['Azerbaijan', 47.7872508, 40.3936294],
# ['Belarus', 27.6971358, 53.4250605], ['Belgium', 4.6667145, 50.6402809], ['Bosnia', 17.5961467, 44.3053476],
# ['Croatia', 17.0118954, 45.5643442], ['Czech Republic', 15.4749544, 49.8167003], ['Denmark', 10.3333283, 55.670249],
# ['Estonia', 25.3319078, 58.7523778], ['Finland', 25.9209164, 63.2467777], ['France', 1.8883335, 46.603354],
# ['Georgia', 44.0287382, 41.6809707], ['Germany', 10.4234469, 51.0834196], ['Gibraltar', -5.3352772, 36.106747],
# ['Greece', 21.9877132, 38.9953683], ['Herzegovina', 17.5961467, 44.3053476], ['Hungary', 19.5060937, 47.1817585],
# ['Iceland', -18.1059013, 64.9841821], ['Ireland', -7.9794599, 52.865196], ['Israel', 34.8667654, 31.5313113],
# ['Italy', 12.674297, 42.6384261], ['Latvia', 24.7537645, 56.8406494], ['Lithuania', 23.7499997, 55.3500003],
# ['Luxembourg', 6.1296751, 49.8158683], ['Monaco', 7.4242474, 43.7384402], ['Netherlands', 5.7480821, 52.5001698],
# ['North Macedonia', 21.7168387, 41.6171214], ['Norway', 9.0999715, 60.5000209], ['Poland', 19.134422, 52.215933],
# ['Portugal', -7.8896263, 40.0332629], ['Romania', 24.6859225, 45.9852129], ['Russia', 97.7453061, 64.6863136],
# ['San Marino', 12.458306, 43.9458623], ['Serbia', 21.0765743, 44.0243228], ['Slovenia', 14.4808369, 45.8133113],
# ['Spain', -4.8380649, 39.3262345], ['Sweden', 14.5208584, 59.6749712], ['Switzerland', 8.2319736, 46.7985624],
# ['Ukraine', 31.2718321, 49.4871968], ['United Kingdom', -3.2765753, 54.7023545], ['Bhutan', 90.5119273, 27.549511],
# ['India', 78.6677428, 22.3511148], ['Nepal', 84.0917139, 28.1083929], ['Sri Lanka', 80.7137847, 7.5554942],
# ['Thailand', 100.83273, 14.8971921], ['Australia', 134.755, -24.7761086], ['Cambodia', 104.869423, 13.5066394],
# ['China', 104.999927, 35.000074], ['Hong Kong', 114.1628131, 22.2793278], ['Indonesia', 117.8902853, -2.4833826], 
# ['Japan', 139.2394179, 36.5748441], ['Macau', 113.5514142, 22.1757605], ['Malaysia', 102.2656823, 4.5693754],
# ['New Zealand', 172.8344077, -41.5000831], ['Philippines', 122.7312101, 12.7503486], ['Republic of Korea', 127.6961188, 36.638392],
# ['Singapore', 103.8303918, 1.340863], ['Taiwan', 120.9820179, 23.9739374], ['Vietnam', 108.4265113, 13.2904027]]
def setup(countries):
    plt.title('Scatter Plot', fontsize=20)
    plt.xlabel('longitude', fontsize=15)
    plt.ylabel('latidude', fontsize=15)
    plt.show()
def draw(countries):
    plt.cla()
    labels,xs,ys = zip(*countries)
    plt.plot(xs, ys, marker = 'o')
    for label, x, y in zip(labels, xs, ys):
        plt.annotate(label, xy = (x, y))
    fig.canvas.draw()
plt.ion()
fig = plt.figure()
MaxGen = 100
mutationRate = 0.2
totalCountries =len(countries)
populationSize = 400
populationData = InitialPopulation(countries,populationSize)
BestEver = populationData[0]	
bestDist = RelativeTotalDist(BestEver)
setup(BestEver)
for i in range(MaxGen):
    fitness=[]
    for order in populationData:
	    d = RelativeTotalDist(order)
	    if d < bestDist:
		    bestDist= d
		    BestEver = order
	    fitness.append(1/d)
    fitnessNormalized = [order/sum(fitness) for order in fitness]
    populationData = NextPopulation(populationData,fitnessNormalized,mutationRate)
    print(bestDist)
    draw(BestEver)
    plt.pause(0.0001)
print(TotalDist(BestEver),BestEver)
with open('BestPath.txt','a+') as af:
    af.write(f'{BestEver},{TotalDist(BestEver)}')
