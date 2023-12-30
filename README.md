# OIBSIB_task-2

1. **User Input Function (`take_input()`):**
   - This function runs in a loop, prompting the user to enter their weight and height in kilograms and meters, respectively.
   - It ensures that the entered values are positive numbers and handles exceptions for invalid inputs.

2. **BMI Calculation Function (`calculate_body_mass_index(weight, height)`):**
   - This function takes the user's weight and height as parameters and calculates the BMI using the formula: BMI = weight / (height^2).

3. **BMI Categorization Function (`categorize_body_mass_index(bmi)`):**
   - This function categorizes the calculated BMI into different weight status categories.
   - The categories are defined based on standard BMI ranges for Underweight, Normal weight, Overweight, and Obese.

4. **Main Program (`main_program()`):**
   - The main program calls the `take_input()` function to get the user's weight and height.
   - It then calls the `calculate_body_mass_index()` function to compute the BMI.
   - The BMI is then passed to the `categorize_body_mass_index()` function to determine the weight status category.
   - The program prints the user's BMI and the corresponding weight status category.

5. **Execution Block (`if __name__ == "__main__":`):**
   - The main execution block creates an entry point for the script.
   - It calls the `main_program()` function when the script is run, initiating the entire BMI calculation and categorization process.

