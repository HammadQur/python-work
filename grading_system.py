# Function to assign grades based on marks
def assign_grade(marks):
    if marks >= 95:
        return "A+1"
    elif marks >= 85:
        return "A"
    elif marks >= 75:
        return "B+"
    elif marks >= 65:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 45:
        return "D"
    else:
        return "F"

# Function to return truth value for a specific condition (e.g., grade A)
def check_truth_value(grade):
    if grade == "A+1":
        return True
    else:
        return False

# Main program
def grading_system():
    # Take user input for marks
    marks = float(input("Enter the marks of the student: "))

    # Call the function to assign grade
    grade = assign_grade(marks)

    # Check if the grade is A and return True/False
    result = check_truth_value(grade)

    # Display the grade and truth value result
    print(f"The grade for marks {marks} is: {grade}")
    print(f"Is the grade A? {result}")

# Call the grading system function
grading_system()
