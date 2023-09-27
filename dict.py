# dict cars
cars = {'color': 'black', 
        'model': 'toyota', 
        'year': '2010',}

# add key & value to a dictionary
cars['price'] = 5998.97

# convert price float to price int
# print(int(cars['price']))

# modification
# cars['color'] = 'red'
# print(cars.get('color'))

# delete a value
# del cars['price']

# loop thr' a dict to get the keys
# for key in cars.keys():
#         print(key)

# loop thr' a dict to get the values
# for value in cars.values():
#         print(value)

# str(cars['price'] ) to convert/cast float to string                                                                                               
print( 'I have a ' + cars['color'] + ' ' + cars['model'] + ' ' + cars['year'] + 'model that is ' + str(cars['price']) + ' dollars')

# loop thr' a dict and get keys & values
for key, value in cars.items():
        # str(value) to cast price float --> 5998.97 to price string
        print(key + ' ' + str(value))
