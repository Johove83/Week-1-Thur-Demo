name = input("Welcome to the Boba Shop! What is your name?\n\n")
sweetness = ""
if name != "":
    print("\n\nHello, " + name + ".\n\n")
    beverage = input("\n\nWhat kind of boba drink would you like?\n\n")
    sweetness_level = input("\n\nHow sweet do you want your drink: 0, 50, 100, or 200?\n\n")
    if sweetness_level == str(50):
        sweetness = "half sweetened"
    elif sweetness_level == str(100):
        sweetness = "normal sweet"
    elif sweetness_level == str(200):
        sweetness = "super sweet"
    else:    
        sweetness = "non-sweet"     
    print(f"Your order of {beverage} boba with a sweet level of {sweetness} will be out shortly.")
else:
    print("You didn't give us your name! Goodbye.")
    
    

#issues until I realized I must convert integers into strings.
