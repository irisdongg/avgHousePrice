import requests
from bs4 import BeautifulSoup

query_city = input('Which zipcode ')
query_zone = input('Which zone ') 

r = requests.get(f'https://{query_zone}.craigslist.org/search/apa?sort=dist&availabilityMode=0&postal={query_city}&search_distance=4')

soup = BeautifulSoup(r.text, 'html.parser')

html = soup.find('div', {'class': 'content'})
spans = html.find_all('span', {'class' : 'result-price'})

count = 0 
total = 0 
for s in spans:
    val = s.text.strip('$') 
    total  = total + int(val) 
    count = count + 1

print('The average value of ' + query_city + ' is $' + str(total/count)) 


