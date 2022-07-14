#Create a list; and use else-if statements to respond to data inside list
farm = ["pig", "cow", "chicken", "dog", "horse", "sheep"]
if farm[0] != "Godzilla": #Should respond
    print("RWAR!")
elif farm[-1] == "Mothra": #Should not respond
    print("SCREECH")
else:
    print("This animal is neither Godzilla nor Mothra!") #Should not respond
    
    
dog = "Spot"
cat = 0
city = 0
car = 0

cat = "Farley"
city = "San Francisco"
car = "Prius"

print(f"See {dog} run!")
print("I drive " + cat + " around " + city + " in my " + car + ".")

budget = 5000
rent_cost = 1500
utilities_cost = 150
food_cost = 250
transporation_cost = 350
computer_cost = 2000
total_cost = rent_cost + utilities_cost + food_cost + transporation_cost + computer_cost
if budget > total_cost:
    print(f"Your total cost is {total_cost}.")
else:
    print(f"You are over budget by {total_cost - budget}.")

if rent_cost > utilities_cost + food_cost + transporation_cost:
    print("You are not eating well enough!")
else:
    print("Ahhh just right!")