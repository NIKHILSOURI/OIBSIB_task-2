def take_input():
    while True:
        try:
            user_weight = float(input("Enter your weight in kilograms: "))
            user_height = float(input("Enter your height in meters: "))
            if user_weight > 0 and user_height > 0:
                return user_weight, user_height
            else:
                print("Please enter valid positive values for weight and height.")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

def calculate_body_mass_index(weight, height):
    return weight / (height ** 2)

def categorize_body_mass_index(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main_program():
    user_weight, user_height = take_input()
    user_bmi = calculate_body_mass_index(user_weight, user_height)
    bmi_category = categorize_body_mass_index(user_bmi)

    print(f"\nYour BMI is: {user_bmi:.2f}")
    print(f"Category: {bmi_category}")

if __name__ == "__main__":
    main_program()
