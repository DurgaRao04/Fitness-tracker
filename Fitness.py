def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def fitness_level(bmi, age, gender):
    gender = gender.lower()
    
    if age < 18:
        return "BMI interpretation for minors requires growth charts. Not covered."
    
    # Define thresholds with slight differences in wording by gender
    if 18 <= age <= 24:
        if bmi < 18.5:
            return "Underweight – Improve nutrition"
        elif 18.5 <= bmi < 24.9:
            return "Healthy – Good fitness level"
        elif 25 <= bmi < 29.9:
            return "Overweight – Consider improving fitness"
        else:
            return "Obese – Needs lifestyle changes"
    
    elif 25 <= age <= 45:
        if bmi < 18.5:
            return "Underweight – Below average fitness"
        elif 18.5 <= bmi < 25:
            return "Normal – Good fitness level"
        elif 25 <= bmi < 30:
            return "Overweight – Work on diet and exercise"
        else:
            return "Obese – Increased health risk"
    
    elif age > 45:
        if bmi < 18.5:
            return "Underweight – Monitor nutrition closely"
        elif 18.5 <= bmi < 26:
            return "Normal – Healthy weight range"
        elif 26 <= bmi < 30:
            return "Slightly Overweight – Lifestyle check recommended"
        else:
            return "Obese – High health risk"
    
    return "Unable to determine fitness level"

# Example usage
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ")

    bmi = calculate_bmi(weight, height)
    level = fitness_level(bmi, age, gender)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Fitness Level Assessment: {level}")
except ValueError:
    print("Invalid input. Please enter numerical values for weight, height, and age.")
