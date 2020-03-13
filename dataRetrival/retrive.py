import requests
APIKEY = '0c7afe19f93e488aaccb79e0a1e3b1e0'

countriesList =['Algeria', 'Nigeria', 'Senegal', 'South Africa', 'Americas', 'Argentina', 'Brazil', 'Canada', 'Chile', 'Dominican Republic', 'Ecuador', 'Guadalupe', 'Mexico', 'United States', 'Afghanistan', 'Bahrain', 'Egypt', 'Iran', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Morocco', 'Oman', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Tunisia', 'United Arab Emirates', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Herzegovina', 'Hungary', 'Iceland', 'Ireland', 'Israel', 
'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Monaco', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Bhutan', 'India', 'Nepal', 'Sri Lanka', 'Thailand', 'Australia', 'Cambodia', 'China', 'Hong Kong', 'Indonesia', 'Japan', 'Macau', 'Malaysia', 'New Zealand', 'Philippines', 'Republic of Korea', 'Singapore', 'Taiwan', 'Vietnam']
#OSM,mlat&mlon


LatLonContries = {}
for country in countriesList:
    url = f'https://api.opencagedata.com/geocode/v1/json?q={country}&key={APIKEY}&limit=1'
    r = requests.get(url)
    LatLonContries[country] = r.json()['results'][0]['geometry']


print(LatLonContries)
    
'''
for country in countriesList:
    url = f'https://api.opencagedata.com/geocode/v1/json?q={country}&key={APIKEY}'
'''

