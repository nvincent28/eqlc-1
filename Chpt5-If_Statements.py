cars = []

cars.append('Volkswagon')
cars.append('Tesla') 
cars.append('Nissan') 
cars.append('Acura') 
cars.append('Suburu')
cars.append('bmw')  

print (cars)

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


request_topping = 'mushrooms'

if request_topping != 'anchovies':
	print("Hold the anchovies!")

answer = 17

if answer != 42:
	print("That is not the correct answer.  Please try again!")

age_0 = 2
age_1 = 22

if age_0 >= 21 and age_1 >= 21:
	print("True")
else:
	print("False")


requested_toppings = ['mushrooms','onions','pineapples']

if 'pepperoni' in requested_toppings:
	print("True")
else:
	print("False")

#banned_users.py

banned_players = ['sally','laimbeer','mahorn','rodman']
user = 'rodman'

if user not in banned_players:
	print(f"{user.title()}, you can get back into the game.")
else:
	print("Everyone is banned!")
#Conditional Tests

car = 'Suburu'
print("Is car == 'Suburu'? I predict True.")
print(car == 'Suburu')

print("\nIs car == 'Acura'? I predict False.")
print(car == 'Acura')

age = 90

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost is ${price}.")



count_tenthous = [value+1 for value in range(0, 10000)]

print("Is there a number 588 == 'count_tenthous'? I predict True.")
print(count_tenthous[:] == '588')

print("\nIs car == 'Acura'? I predict False.")
print(count_tenthous == '600000')


basket = 10

if basket == 4:
	player = 'Crawford'
	print(f"{player} for {basket}.")
elif basket == 3:
	player = 'Curry'
	print(f"{player} for {basket}.")
elif basket == 2:
	player = 'James'
	print(f"{player} for {basket}.")
elif basket == 1:
	player = 'Harden'
	print(f"{player} for {basket}.")
else:
	print(f"Missed basket.")


age = -11

if age < 2:
	stage = 'baby'
	print(f"{age} is a {stage}.")
elif age == 2 or age < 5:
	stage = 'toddler'
	print(f"{age} is a {stage}.")
elif age == 4 or age < 13:
	stage = 'kid'
	print(f"{age} is a {stage}.")
elif age == 13 or age < 20:
	stage = 'teenager'
	print(f"{age} is a {stage}.")
elif age == 20 or age < 65:
	stage = 'adult'
	print(f"{age} is a {stage}.")
elif age == 65 or age > 65:
	stage = 'elder'
	print(f"{age} is a {stage}.")
else:
	print(f"Alien being")


# USING IF STATEMENTS WITH LISTS

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['pickled pigfeet','french fries','bon bon lomidon']


for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


#User Admin Code

new_users = ['Jwilliams','Scurry','Ljames','soneal','kdurant']

users = ['jwilliams','bwallace','ljames','mjordan','kbryant','pewing']

for new_user in new_users:
	if new_user.lower() in users:
		print(f"Sorry, the following username: {new_user} is not available.  Please try again.")
	else:
		print(f"Success! The following username: {new_user} is available.")

print("\nPlease select your next function.")

#Numbering System

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print(f"\n{number}st")
	elif number == 2:
		print(f"\n{number}nd")
	elif number == 3:
		print(f"\n{number}rd")
	else:
		print(f"\n{number}th")

print(numbers)
