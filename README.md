# Fitness-tracker
A simple BMI-based fitness tracker that evaluates health levels using age and BMI. It provides personalized feedback and promotes healthy lifestyle choices.

BMI and Fitness Level Assessment
This is a simple Python project that calculates a user's Body Mass Index (BMI) and provides a basic fitness level assessment based on their age, gender, and BMI score.

🔍 Overview
The program:

Prompts the user to input their weight (kg), height (cm), age, and gender.

Calculates BMI using the formula:
BMI = weight (kg) / (height (m)^2)

Evaluates the user's fitness level based on age and BMI categories.

Outputs the BMI value and an interpreted fitness level message.

🚀 How to Run
Clone or download this repository.

Make sure you have Python 3 installed.

Run the script in your terminal or IDE:

bash
Copy
Edit
python bmi_fitness_assessment.py
Follow the prompts and enter:

Weight in kilograms

Height in centimeters

Age in years

Gender (Male/Female)

💡 Example Output
mathematica
Copy
Edit
Enter your weight in kg: 70
Enter your height in cm: 175
Enter your age: 30
Enter your gender (Male/Female): Male

Your BMI is: 22.86
Fitness Level Assessment: Normal – Good fitness level
⚙️ Features
Handles invalid input using try-except.

Provides custom fitness interpretations based on age groups:

18–24

25–45

45+

Treats underage users differently with a special message.

📌 BMI Categories Used
BMI Range	Interpretation
< 18.5	Underweight
18.5 – 24.9	Healthy/Normal
25 – 29.9	Overweight
30 and above	Obese

(Note: Slight variations in interpretation exist based on age.)

🛡️ Limitations
Not suitable for users under 18 — BMI interpretation for minors typically requires growth charts.

Does not account for muscle mass, body composition, or ethnic-specific BMI variations.
