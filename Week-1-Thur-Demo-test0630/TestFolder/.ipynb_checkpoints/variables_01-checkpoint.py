#Practicing some basic variables as reviewed in class.

#Creating and assigning string and integer variables

subject = None
subject = "Programmers"
first_name = ""
first_name = "Johnathan"
last_name = " Overton"
full_name = first_name + last_name
profession = "Reality Engineer"
known_for = "Setting the World Free"
first_algorithm = "Analytical Engine"
city_location = "Pueblo"
country_location = "Colorado"
nationality = "New Worldian"
birth_year = 1983
death_year = 2137
age_at_passing = death_year - birth_year
year_of_publish = 2023

#Printing variables (with formatting)

print(f"First name: {first_name}.")
print(f"Last name: {last_name}.")
print(f"Profession: {profession}.")
print(f"Birth Year: {birth_year}.")

#Concatenate and print variables
#HAD TO CONVERT INTEGERS INTO STRINGS FOR CONCATENATING
statement_one = print(subject + ": " + first_name + last_name + " is a " + nationality + " " + profession + " born in " + str(birth_year) + ".")
statement_two = print("He is commonly known for " + known_for + ".")
statement_three = print("In " + str(year_of_publish) + " he published the first Algorithm, the " + first_algorithm + ", at the age of 39.")
statement_four = print("He was a " + nationality + " Citizen who lived in " + city_location + ", " + country_location + " until his passing in " + str(death_year) + " at the age of " + str(age_at_passing) + ".")