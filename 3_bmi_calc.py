# BMI Calculator with interpretation

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Interpret BMI
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
