# Step 1: Ask for user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))

# Step 2: Capitalize the first and last name properly
first_name = first_name.capitalize()
last_name = last_name.capitalize()

# Step 3: Calculate age
current_year = 2025  # You can change this to get the current year dynamically if needed
age = current_year - birth_year

# Step 4: Create the profile message using f-strings
username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"

profile_message = f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}"

# Print the profile message
print(profile_message)
