# dan Smestad video instructions lab2 

from datetime import datetime, date, time


today = date.today()# prints current date.
print(today)

tomorrow = date(2022 , 1, 16) #date object with consructor usage iso format.
print(tomorrow)

next_week = date.fromisoformat('2022-01-23') #date from a string ISO format.
print(next_week)

# time stamps.

right_now = datetime.now() #time right now, now function. 
print(right_now) #print to the fractions od a second.

print(right_now.timestamp())# time since January 1 to 1970 UTC.

my_date = datetime.fromtimestamp(1500000000)# day object float( or (int(number) is made up
print(my_date)# you can save this and use it to a point in time in a pogram.

import time; # had to import time here to correct errors but time is imported above.

curtime = time.localtime(time.time())# breakout of time intervals. year to \

print("Current Time is:", curtime)

ticktock = time.time()

print('Number of ticks:', ticktock) # number of ticks UTC.

#Tuples - data doesn't change immutable.

#city state good examples they don't/wouldn't change like a float or Intger might.
# example the population will change for these cities .
city_state = [('Seattle', 'WA'), ('Portland','OR'), ('San Fransico', 'CA')]
print(len(city_state))

first_city_state = city_state[0] #prints index 0
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state = first_city_state #unpack to just the city .
#print(city).
print(state) # prints state.

# more unpacking - need enough variaels to unpack it.
animals = ('lion', 'puma', 'tiger')

lion, puma ,tiger = animals

print(animals)
print(tiger)

#returning more than one value or a function.

def get_distance(): # creating a new function, a non-system function.
    miles = 10000
    km =miles * 1.6
    return miles, km  #returns distnce in kilo meters.

distances = get_distance()
print(distances)  #use index to get just the miles.
# output showing parh like this (10000, 16000.0).

# rewritten here with an unpacking method
miles, km = get_distance()
print(km) #get the kilo meters for us.

'''# Sets  - new set() - Sets will prevent duplicates. order is not order or not a gauranteed logical order.
# unordered collection'''
cats = set() # creating an emtpy set.
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')# gets added to first index. Claras was added to the last index -1.
print(cats)

birds = {'owl', 'robin', 'swan'} #sets using curly braces.
print(birds)
birds.add('robin')
print(birds)
birds.remove('owl')
birds.add('cardinal') #cardinal add to last position now and. 
print(birds) #position not guaranteed.

for bird in birds: # prints each on new line until conpleted the though the set().
    print(bird)

bird_list = ['owl', 'robin', 'swan', 'swan','eagle', 'cardinal','swan']
print(bird_list)# list with all birds in list w/duplicates
bird_list_no_duplicates = list(set(bird_list))
# covert to set and remove these duplicate swans.
# list convert to a set(), and set by default removes dups from the newly created set.
print(bird_list_no_duplicates) 

#useful for returning multiple values from a function.
# def get_ramdom_bird_pattern():
#     return 'owl', 'cardinal' #returns a tuple.

# bird_pattern = get_ramdom_bird_pattern()
# print(bird_pattern)
# #if you prefer you can do this but it's usually more work.
# #bird, pattern = get_ramdom_bird_pattern_and_pattern()

# data = get_ramdom_bird_pattern
#  # try except : error handling.
# try: 
#     print(data[6]) #index is out of range.
# except:
#     print('oops, that is out of range.') #this did run in seperate python terminal seperated.


