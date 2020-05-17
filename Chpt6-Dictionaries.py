# alien.py

alien_0 = {'color': 'green','points':5}

print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color': 'green','points':5}
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("Beginning of ALIEN MOVEMENT.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['speed'] = 'medium'

print("adding alien speed...")
print(alien_0)

print(f"Original x position: {alien_0['x_position']}.")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")


alien_0['speed'] = 'fast'
alien_0['points'] = 5

print("changing alien speed...")
print(alien_0)

print(f"Original x position: {alien_0['x_position']}.")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")

del alien_0['points']
print("erasing points...")
print(alien_0)


#DICTIONARY OF SIMILAR OBJECTS

favorite_moves = {
	'Jabbar' : 'Sky hook',
	'Bird' : '3-Pointer',
	'Jordan' : 'Up and under',
	'Barkley' : 'Monster Jam',
}

move = favorite_moves['Jordan'].title()
print(f"Jordan's favorite move is {move}")

#USING get()

print("\n\n#################### Using USING get(). ##############")

print("adding alien position...")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print("adding alien speed...")
alien_0['speed'] = 'medium'
print(alien_0)

point_value = alien_0.get('points', 'No point value assigned.')

print(f"Original x position: {alien_0['x_position']}.")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#TRY IT YOURSELF

user_1 = {'fname': 'Grant','lname': 'Avery'}

print(user_1["fname"])
print(user_1["lname"])

print(user_1)

user_1['current'] = 'Xavier School of Gifted'
user_1['future'] = 'X-Force'

print(user_1)

user_1['power1'] = 'Super strength'
user_1['power2'] = 'Flight'
user_1['nickname'] = 'TopFlight'

print(user_1)
third_power = user_1.get('power3', 'No third power.')
print(third_power)

print("\n\n#################### Creating Glossary. ##############")

glossary = {
	'Fontana' : 'a city in San Bernardino County, California. Founded by Azariel Blanchard Miller in 1913,[1] it remained essentially rural until World War II, when entrepreneur Henry J. Kaiser built a large steel mill in the area. It is now a regional hub of the trucking industry, with the east-west [Interstate 10 in California|Interstate 10]] and State Route 210 crossing the city and Interstate 15 passing diagonally through its northwestern quadrant.',
	'Colton' : 'Colton is a city in San Bernardino County, California, United States. Nicknamed "Hub City", it is located in the Inland Empire region of the state and is approximately 57 miles (92 km) east of Los Angeles. The population of Colton is 52,154 according to the 2010 census, up from 47,662 at the 2000 census.',
	'Bloomington' : 'Bloomington is a census-designated place (CDP) in San Bernardino County, California, United States. The population was 23,851 at the 2010 census, up from 19,318 at the 2000 census.'
}

city = glossary['Fontana']
print(f"Fontana : \n{city}\n\n")


#LOOPING THROUGH A DICTIONARY
print("\n\n#################### LOOPING THROUGH A DICTIONARY ##############")


user_1 = {'fname': 'Grant','lname': 'Avery'}
user_1['current'] = 'Xavier School of Gifted'
user_1['future'] = 'X-Force'
user_1['power1'] = 'Super strength'
user_1['power2'] = 'Flight'
user_1['codename'] = 'TopFlight'

for key, value in user_1.items():
	print(f"\nKey:  {key}")
	print(f"\nValue:  {value}")

for name in user_1.keys():
	print(name.title())


#LOOPING THROUGH A DICTIONARY
print("\n\n#################### LOOPING THROUGH A DICTIONARY ##############")

glossary = {
	'Fontana' : 'a city in San Bernardino County, California. Founded by Azariel Blanchard Miller in 1913,[1] it remained essentially rural until World War II, when entrepreneur Henry J. Kaiser built a large steel mill in the area. It is now a regional hub of the trucking industry, with the east-west [Interstate 10 in California|Interstate 10]] and State Route 210 crossing the city and Interstate 15 passing diagonally through its northwestern quadrant.',
	'Colton' : 'Colton is a city in San Bernardino County, California, United States. Nicknamed "Hub City", it is located in the Inland Empire region of the state and is approximately 57 miles (92 km) east of Los Angeles. The population of Colton is 52,154 according to the 2010 census, up from 47,662 at the 2000 census.',
	'Bloomington' : 'Bloomington is a census-designated place (CDP) in San Bernardino County, California, United States. The population was 23,851 at the 2010 census, up from 19,318 at the 2000 census.',
	'Rialto' : 'Rialto is a city in San Bernardino County, California, United States. The population was 99,171 as of the 2010 Census.[11] Rialto is home to major regional distribution centers: Staples Inc., which serves stores across the entire West Coast of the United States, Amazon (company), Under Armour, Medline Industries, Niagara Bottling, Monster Energy and Target in the northern region of the city, in the Las Colinas community.',
	'Ontario' : 'Ontario is a city located in southwestern San Bernardino County, California, 35 miles (56 km) east of downtown Los Angeles and 23 miles (37 km) west of downtown San Bernardino, the county seat. Located in the western part of the Inland Empire metropolitan area, it lies just east of Los Angeles County and is part of the Greater Los Angeles Area. As of the 2010 Census, the city had a population of 163,924, up from 158,007 at the 2000 census.'
}

for key, value in glossary.items():
	print(f"\nCity name:  {key}")
	print(f"\nDescription:  {value}")



print("\n\n#################### Find out  ##############")

favorite_languages = {'peter' : 'python','deborah' : 'c','douglas' : 'ruby','nathan' : 'python'}

for name in sorted(favorite_languages.keys()):
	print(f"Hi {name.title()}.")

print("\n\n#################### NESTING  ##############")

alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)


#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens.

for alien_number in range(30):
	new_alien = {'color':'green','points':'5','speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
#show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Store information about a pozza being ordered

pizza = {
	'crust':'thick',
	'toppings': ['mushrooms','extra cheese'],
}

#Summmarize the order

print(f"You ordered a {pizza['crust']}-crust pizza"
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

print("\n\n#################### Favorite Languages  ##############")


favorite_languages = {
	'peter' : ['python','ruby'],
	'deborah' : ['c','haskell'],
	'douglas' : ['ruby','c#'],
	'nathan' : ['python','c'],
	}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
		
	for language in languages:
			print(f"\t{language.title()}")


print("\n\n#################### MANY USERS  ##############")

users = {
	'mjordan': {
	'first': 'michael',
	'last': 'jordan',
	'location': 'charlotte',
	'nickname': 'Air'},

	'ejohnson': {
	'first': 'earvin',
	'last': 'johnson',
	'location': 'los angeles',
	'nickname': 'Magic',},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")