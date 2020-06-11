"""
Task 1¶
You need to add the cities listed below by modifying the given structure. Cities to add:

Bangalore (India, Asia)
New Delhi (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
Be careful, while adding a city in an existing country. Consider adding it to the existing list of cities as:

locations['Asia']['India'].append('New Delhi')
Task 2
Print the following (using "print") by looking them up in the structure.

A list of all cities in the USA in alphabetic order.
All cities in Asia, in alphabetic order, next to the name of the country. In your output, label each answer with a number so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country
"""
#Task 1
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

#Task 2
print (1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

print (2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)