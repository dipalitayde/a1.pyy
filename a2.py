height = float(input("Enter your height in cm:"))
weight = float(input("Enter you weight in kg :"))

BMI = weight / (height/100)**2

print("your BMI is ", BMI)

if BMI <= 18.4:
    print("you are under weight")

elif BMI <= 24.9 :
    print("Your are healthy")

elif BMI <= 29.9 :
    print("you are over weighted")

elif BMI <= 34.9 :
    print("you are severely over weight.")

elif BMI <= 39.9 :
    print("You are obese.")

else: 
    print("you are severley obese")