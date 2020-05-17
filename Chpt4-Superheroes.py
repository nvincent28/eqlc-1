Guest1 = "Kobe Bryant"
Guest2 = "Michael Jordan"
Guest3 = "Magic Johnson"
Guest4 = "Shaquille O'Neal"
Guest5 = "Charles Barkley"

guest_list=[Guest1, Guest2, Guest3, Guest4, Guest5]
for guest in guest_list:
	print(guest)


superheroes=['Spider-Man','Wolverine','Thor','Cyclops']
for superhero in superheroes:
	print(f"{superhero.title()}, that was a great save!")
	print(f"Who are you going to save next, {superhero.title()}?")

print(f"Great effort team, we saved the planet from disaster!")

pizza1 = "Plain"
pizza2 = "Vegetarian"
pizza3 = "Margarita"
pizza4 = "Meat Lovers"
pizza5 = "Deluxe"

pizzas=[pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
	print(f"I love {pizza.title()} pizza!")

print(f"Gosh I love all types of pizza!")


#for value in range(1, 1000):
#	print(value)

#numbers = list(range(1,100, 15))
#print(numbers)


#TWO APPROACHES TO CODING ----------------------------
#Approach 1:  This is easier to read!!
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print (squares)

#Approach 2:  This is more efficient!
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print (squares)

#KEY POINT:  
#Step 1 - Focus first on writing code that you understand clearly.  
#Step 2 - Then look for more efficient approaches as you review your code.

#Simple Statistics with a List of Numbers

digits = [123453, 4, 92, 16, 3325, 136, 49, 64, 81, 1001, 41, 97, 156756, 25, 2336, 49, 64, 81, 100]

print(min(digits))
print(max(digits))
print(sum(digits))

#Approach 3:  in this case, it is the most efficient!
squares = [value**2 for value in range(1, 11)]
print (squares)

count20 = [value+1 for value in range(0, 20)]
print (count20)

count_million = [value+1 for value in range(0, 1000000)]

print(min(count_million))
print(max(count_million))
print(sum(count_million))

count20_odd = [value+1 for value in range(0, 20, 2)]
print (count20_odd)

count20_by3 = [value+3 for value in range(0, 30, 3)]
print (count20_by3)

count_cubed = [value**3 for value in range(0, 10)]
print (count_cubed)

#
#WORKING WITH PART OF A LIST
#
superheroes=['Spider-Man','Wolverine','Thor','Cyclops','Captain America']
print(superheroes[0:3])
print(superheroes[1:4])
print(superheroes[:4])
print(superheroes[2:])
print(superheroes[-3:])

#
#COPYING A LIST
#

my_favorite_foods = ['duri a pwa', 'lambi', 'bunnun fri', 'grio']
hawkins_foods = my_favorite_foods[:]

print("My favorite foods are:")
print(my_favorite_foods)

print("\nMy friend's favorite foods are:")
print(hawkins_foods)

my_favorite_foods.append('legume')
hawkins_foods.append('paté kodé')

print("My favorite foods are:")
print(my_favorite_foods)

print("\nMy friend's favorite foods are:")
print(hawkins_foods)

pizza1 = "Plain"
pizza2 = "Vegetarian"
pizza3 = "Margarita"
pizza4 = "Meat Lovers"
pizza5 = "Deluxe"

pizzas=[pizza1, pizza2, pizza3, pizza4, pizza5]

print("My 3 first favorite pizzas are:")
print(pizzas[:3])

print("My 3 middle favorite pizzas are:")
print(pizzas[1:4])

print("My 3 last favorite pizzas are:")
print(pizzas[-3:])


mvp1 = "Kobe Bryant"
mvp2 = "Michael Jordan"
mvp3 = "Magic Johnson"
mvp4 = "Shaquille O'Neal"
mvp5 = "Charles Barkley"

mvp_nate=[mvp1, mvp2, mvp3, mvp4, mvp5]
mvp_hawk = mvp_nate[:]

mvp_nate.append('Kevin Durant')
mvp_hawk.append('Lebron James')

for mvp in mvp_nate:
	print(mvp)

for mvp in mvp_hawk:
	print(mvp)


#
#DEFINING A TUPLE:  An immutable dataset
#	

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions.append(300)
