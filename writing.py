# cities = ["New York", "Los Angeles", "San Francisco", "Chicago", "Portland"]
#
# with open("C:/Users/admin/Desktop/cities.txt",'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []

with open("C:/Users/admin/Desktop/cities.txt",'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

