height = float(input('Plaese input your Heightin meters: '))
weight = float(input('Plaese input your Weight in kg: '))
bmi = (weight / (height*height))

if (bmi > 0 and bmi <= 18.5):
    print(round(bmi,2))
    print('You are undeweight')
elif (bmi > 18.5 and bmi <= 24.9):
    print(round(bmi,2))
    print('Your  BMI is normal')
elif (bmi >25 and bmi<= 29.9):
    print(round(bmi,2))
    print('You are overweight')
elif (bmi >= 30 and bmi <= 34.9):
    print(round(bmi,2))
    print('You have type I Obesity')            
elif (bmi >= 35 and bmi <= 39.9):
    print(round(bmi,2))
    print('You have type II Obesity')
else: 
    print(round(bmi,2))
    print('You are extremely obese')    
