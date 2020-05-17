car = input("What car did you like to rent?\n:")
print(f"We will check our inventory for a {car}.")


party = input("How many in your party?\n:")
party = int(party)

if party <= 8:
	print("\nYour table is ready!")
else:
	print("\nWe need time to make sure we have comfortable space for your party.")

number = input("Enter a number to be evaluated as a divisible by 10.\n:")
number = int(number)

if number % 10 == 0:
	print (f"\nThe number {number} is multiple10")
else:
	print (f"\nThe number {number} is not multiple10")


#####################################

message = ""

while message != 'quit':
	message = input(prompt)
	print(message)


active = True
while active:
	message = input(prompt)

		if message == 'quit':
			active = False
		else:
			print(message)

#######################

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:

	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")


current_number = 0

while current_number < 10:
	current_number += 1
	
	if current_number % 2 == 0:
		continue
	print(current_number)



prompt = "\nPlease enter the pizza topping you would like to add:"
prompt += "\n(Enter 'quit' when you are finished.) "
toppings = []

while True:

	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		toppings.append(topping)
		print(f"Adding {topping.title()}!")
		print(f"Your pizza now has {toppings}!")



##############################


prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:

	age = input(prompt)
	age = int(age)

	if age == 'quit':
		break
	else:
		if age < 4:
			price = 0
		elif age < 18:
			price = 25
		elif age < 65:
			price = 40
		else:
			price = 20
			
		print(f"Your admission cost is ${price}.")

#################### 

current_number = 2

while current_number <= 10:
	print(current_number)

##################

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
	print(confirmed_user.title())


################# 

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

##################

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary.
	responses[name] = response

# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
	print(f"{name} would like to climb {response}.")