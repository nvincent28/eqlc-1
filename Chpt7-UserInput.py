# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
sandwich_orders = ['Italian Hotdog','Cheeseburger','Hot Pastrami','Hot Pastrami','Philly Cheesesteak','Hot Pastrami',]
	
print(sandwich_orders)

finished_sandwiches = []

while 'sandwich_order' in sandwich_orders:
	sandwich_orders.remove('Hot Pastrami')
	print(f"Our apologies.  We are out of Hot Pastrami.")


# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while sandwich_orders:
	current_order = sandwich_orders.pop()
	print(f"Verifying order: {current_order.title()}")
	finished_sandwiches.append(current_order)

# Display all confirmed users.
print("\nThe following sandwiches are ready to be served:")

for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())
