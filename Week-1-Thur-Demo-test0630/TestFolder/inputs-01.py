#Allowing user input

welcome_name = input("Welcome to the sandwich shop, what do I call you?\n\n")

print("Hello " + welcome_name + ".")

question_sandwich = input("Are you here for a sandwich?\n\n").lower()

if question_sandwich == "yes":
    food_prompt = input("What kind of sandwich would you like?\n\n")
    print(f"Please wait 10 minutes for your {food_prompt}.")
else:
    print("If you do not want a sandwich what are you here for?")

    
#took a moment to allow capitalized and uncapitalized inputs to allow appropriate response
    