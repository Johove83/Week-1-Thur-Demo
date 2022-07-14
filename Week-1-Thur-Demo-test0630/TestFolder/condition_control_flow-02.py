#character 1

c1_name = "Mr. Farley"
c1_age = 65
c1_profession = "Web Developer"
c1_salary = 100000.00
c1_species = "cat"
c1_location = "San Francisco, CA"
c1_monthly_rent = 2000
c1_monthly_expenses = 1500
c1_yearly_rent = c1_monthly_rent * 12
c1_yearly_expenses = c1_monthly_expenses * 12
c1_savings = c1_salary - (c1_yearly_rent + c1_yearly_expenses)

#character 2

c2_name = "Mr. Snuggles"
c2_age = 30
c2_profession = "Accountant"
c2_salary = 70000
c2_species = "mouse"
c2_location = "Oakland, CA"
c2_monthly_rent = 4000
c2_monthly_expenses = 500
c2_yearly_rent = c2_monthly_rent * 12
c2_yearly_expenses = c2_monthly_expenses * 12
c2_savings = c2_salary - (c2_yearly_rent + c2_yearly_expenses)

#Comparing people, without judgement of course

if c1_name == "Mr. Farley":
    print(f"Hello {c1_name}.")
else:
    print("Hello stranger.")

#What is age anyway?    
if c2_age > c1_age:
    print(c2_name + "is older than " + c1_name + ".")
elif c1_age > c2_age:
    print(f"{c1_name} is older than {c2_name}.")
else:
    print(c1_name + " and " + c2_name + " are the same age.")
    
if c1_location == "Oakland, CA":
    print(f"{c1_name} comes from the home of the Raiders!")
elif c1_location == "San Francisco, CA":
    print(f"{c1_name} comes from the home of the 49ers.")
else:
    print(f"{c1_name} doesn't hail from a sports town.")
    
#Who pays more rent?

if c1_monthly_rent > c2_monthly_rent:
    print(f"{c1_name} pays more rent than {c2_name}.")
elif c2_monthly_rent > c1_monthly_rent:
    print(f"{c1_name} pays less rent than {c2_name}.")
else:
    print(f"{c1_name} pays the same rent as {c2_name}.")
    
if c1_monthly_expenses > c2_monthly_expenses:
    print(f"{c1_name} has more expenses than {c2_name}.")
elif c1_monthly_expenses < c2_monthly_expenses:
    print(f"{c1_name} pays less expenses than {c2_name}.")
else:
    print(f"{c1_name} pays the same expenses as {c2_name}.")
    
if c1_profession == "Web Developer" and c2_profession == "Accountant":
    print(f"Look a {c1_profession} and an {c2_profession}.")
else:
    print("They are professionals.")


    