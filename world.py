from math import sin, cos, sqrt, atan2, radians ,pow
import pandas as pd
import numpy as np

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
def WithinRadius(lat1,lon1,lat2,lon2,radius):
	distance = distance(lat1,lon1,lat2,lon2)
	if distance < radius:
		return True
	else:
		return False

flightStat = 'https://www.flightstats.com/go/weblet?guid=c228b59beca1b817:1fb62a4f:11502c4a893:6b48&weblet=status&action=display&imageColor=black&language=English'
speed = 835
data = pd.read_csv("airports.csv")
Countries ={'Algeria': {'lat': 28.0000272, 'lng': 2.9999825}, 'Nigeria': {'lat': 9.6000359, 'lng': 7.9999721}, 'Senegal': {'lat': 14.4750607, 'lng': -14.4529612}, 'South Africa': {'lat': -28.8166236, 'lng': 24.991639}, 'Americas': {'lat': 19.1982908, 'lng': -99.5486812}, 'Argentina': {'lat': -34.9964963, 'lng': 
-64.9672817}, 'Brazil': {'lat': -10.3333333, 'lng': -53.2}, 'Canada': {'lat': 61.0666922, 'lng': -107.9917071}, 'Chile': {'lat': -31.7613365, 'lng': -71.3187697}, 'Dominican Republic': {'lat': 19.0974031, 'lng': -70.3028026}, 'Ecuador': {'lat': -1.3397668, 'lng': -79.3666965}, 'Guadalupe': {'lat': 29.6480061, 'lng': -97.8279576}, 'Mexico': {'lat': 19.4326296, 'lng': -99.1331785}, 'United States': {'lat': 39.7837304, 'lng': -100.4458825}, 'Afghanistan': {'lat': 33.7680065, 'lng': 66.2385139}, 'Bahrain': {'lat': 26.1551249, 'lng': 50.5344606}, 'Egypt': {'lat': 26.2540493, 'lng': 29.2675469}, 'Iran': {'lat': 32.6475314, 'lng': 54.5643516}, 'Iraq': {'lat': 33.0955793, 'lng': 44.1749775}, 'Jordan': {'lat': 31.1667049, 'lng': 36.941628}, 'Kuwait': {'lat': 29.2733964, 'lng': 47.4979476}, 'Lebanon': {'lat': 33.8750629, 'lng': 35.843409}, 'Morocco': {'lat': 31.1728205, 'lng': -7.3362482}, 'Oman': {'lat': 21.0000287, 'lng': 57.0036901}, 'Pakistan': {'lat': 30.3308401, 'lng': 71.247499}, 'Qatar': {'lat': 25.3336984, 'lng': 51.2295295}, 'Saudi Arabia': 
{'lat': 25.6242618, 'lng': 42.3528328}, 'Tunisia': {'lat': 33.8439408, 'lng': 9.400138}, 'United Arab Emirates': {'lat': 24.0002488, 'lng': 53.9994829}, 'Andorra': {'lat': 42.5407167, 'lng': 1.5732033}, 'Armenia': {'lat': 40.7696272, 'lng': 44.6736646}, 'Austria': {'lat': 47.2000338, 'lng': 13.199959}, 'Azerbaijan': {'lat': 40.3936294, 'lng': 47.7872508}, 'Belarus': {'lat': 53.4250605, 'lng': 27.6971358}, 'Belgium': {'lat': 50.6402809, 'lng': 4.6667145}, 'Bosnia': {'lat': 44.3053476, 'lng': 17.5961467}, 'Croatia': {'lat': 45.5643442, 'lng': 17.0118954}, 'Czech Republic': {'lat': 49.8167003, 'lng': 15.4749544}, 'Denmark': {'lat': 55.670249, 'lng': 10.3333283}, 'Estonia': {'lat': 58.7523778, 'lng': 25.3319078}, 'Finland': {'lat': 63.2467777, 'lng': 25.9209164}, 'France': {'lat': 46.603354, 'lng': 1.8883335}, 'Georgia': {'lat': 41.6809707, 'lng': 44.0287382}, 'Germany': {'lat': 51.0834196, 'lng': 10.4234469}, 'Gibraltar': {'lat': 36.106747, 'lng': -5.3352772}, 'Greece': {'lat': 38.9953683, 'lng': 21.9877132}, 'Herzegovina': {'lat': 44.3053476, 
'lng': 17.5961467}, 'Hungary': {'lat': 47.1817585, 'lng': 19.5060937}, 'Iceland': {'lat': 64.9841821, 'lng': -18.1059013}, 'Ireland': {'lat': 52.865196, 'lng': -7.9794599}, 'Israel': {'lat': 31.5313113, 'lng': 34.8667654}, 'Italy': {'lat': 42.6384261, 'lng': 12.674297}, 'Latvia': {'lat': 56.8406494, 'lng': 24.7537645}, 'Lithuania': {'lat': 55.3500003, 'lng': 23.7499997}, 'Luxembourg': {'lat': 49.8158683, 'lng': 6.1296751}, 'Monaco': {'lat': 43.7384402, 'lng': 7.4242474}, 'Netherlands': {'lat': 52.5001698, 'lng': 5.7480821}, 'North Macedonia': {'lat': 41.6171214, 'lng': 21.7168387}, 'Norway': {'lat': 60.5000209, 'lng': 9.0999715}, 'Poland': {'lat': 52.215933, 'lng': 19.134422}, 'Portugal': {'lat': 40.0332629, 'lng': -7.8896263}, 'Romania': {'lat': 45.9852129, 'lng': 24.6859225}, 'Russia': {'lat': 64.6863136, 'lng': 97.7453061}, 'San Marino': {'lat': 43.9458623, 'lng': 12.458306}, 'Serbia': {'lat': 44.0243228, 'lng': 21.0765743}, 'Slovenia': {'lat': 45.8133113, 'lng': 14.4808369}, 'Spain': {'lat': 39.3262345, 'lng': -4.8380649}, 'Sweden': {'lat': 59.6749712, 'lng': 14.5208584}, 'Switzerland': {'lat': 46.7985624, 'lng': 8.2319736}, 'Ukraine': {'lat': 49.4871968, 'lng': 31.2718321}, 'United Kingdom': {'lat': 54.7023545, 'lng': -3.2765753}, 'Bhutan': {'lat': 27.549511, 'lng': 90.5119273}, 'India': {'lat': 22.3511148, 'lng': 78.6677428}, 'Nepal': {'lat': 28.1083929, 'lng': 84.0917139}, 'Sri Lanka': {'lat': 7.5554942, 'lng': 80.7137847}, 'Thailand': {'lat': 14.8971921, 'lng': 100.83273}, 'Australia': {'lat': -24.7761086, 'lng': 134.755}, 'Cambodia': {'lat': 13.5066394, 'lng': 104.869423}, 'China': {'lat': 35.000074, 'lng': 104.999927}, 'Hong Kong': {'lat': 22.2793278, 'lng': 114.1628131}, 'Indonesia': {'lat': -2.4833826, 'lng': 117.8902853}, 'Japan': {'lat': 36.5748441, 'lng': 139.2394179}, 'Macau': {'lat': 22.1757605, 'lng': 113.5514142}, 'Malaysia': {'lat': 4.5693754, 'lng': 102.2656823}, 'New Zealand': {'lat': -41.5000831, 'lng': 172.8344077}, 'Philippines': {'lat': 12.7503486, 'lng': 122.7312101}, 'Republic of Korea': {'lat': 36.638392, 'lng': 127.6961188}, 'Singapore': {'lat': 1.340863, 'lng': 103.8303918}, 'Taiwan': {'lat': 23.9739374, 'lng': 120.9820179}, 'Vietnam': {'lat': 13.2904027, 'lng': 108.4265113}}


with open("NewAirport.csv",'w+') as titles:
	titles.write('"id","ident","type","name","latitude_deg","longitude_deg","continent","iso_country","iso_region","gps_code","iata_code","local_code"\n')
	for index, row in data.iterrows():
		if row["type"] in ['large_airport','medium_airport']:
			data.loc[[index],["id","ident","type","name","latitude_deg","longitude_deg","continent","iso_country","iso_region","gps_code","iata_code","local_code"]].to_csv('NewAirport.csv',header=None,mode='a',index=None)


'''
*USing index to get the data from this entry(of latitude_deg) 
print(data.iloc[6]['latitude_deg'])

fields to remove




'''