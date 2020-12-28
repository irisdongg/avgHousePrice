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
















#print(soup.find(id = 'sortable-results').div.find_all('span', {'class': 'result-price'})[0].text)i
#x = (soup.find(class = 'zsg-layout-width zsg-layout-top').div.find(class = 'zsg-content-section region-info').section.find(id = 'tt-hv-metric').div)

#print(x.find('h2'))

#print(soup.find('div', {'class' : 'region-info-item'}).find('h2').text)
#print(soup)
#print(soup.find('div', attrs = {'class': 'col-md-3 px-1'}).findAll('p')[3].text)

#print(soup.find(id = 'topSection').div.find('class' = 'mop-ratings-wrap__half').div.find_all('a')[0].find('span').text)
#find('span', attr = {'class', 'mop-ratings-wrap__percentage'}).text)


