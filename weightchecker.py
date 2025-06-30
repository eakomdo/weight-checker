# A program to determine the weight of a person

while True:

    name = input("Enter your name: ")

    print ("Hello " + name + ". You're welcome to the weight checker program.")

    weight = float(input("Please enter your weight: "))
    unit = input("Is this in pounds or kilograms? (p/k): ")
    
    if weight <= 0:
        print("Invalid weight. Please enter a positive number.")
        continue
    if weight > 1000:
        print("Invalid weight. Please enter a realistic weight (less than 1000).")
        continue         
    
    if unit.lower() == 'p':
        weight = weight * 0.453592  # Convert pounds to kilograms
        print (f"{name}, your weight in kilograms is {weight:.2f} kg.")
        break
    elif unit.lower() == 'k':
        weight = weight / 0.453592  # Convert kilograms to pounds
        print(f"{name}, your weight in pounds is {weight:.2f} lbs.")
        break
   
    elif unit.lower() not in ['p', 'k'] and weight > 0 and weight <= 1000:
        print("Invalid unit. Please enter 'p' for pounds or 'k' for kilograms.")
        continue
    else:
        print("An unexpected error occurred. Please try again.")
        continue 
  

print("Thank you for using the weight checker program. Goodbye!")
input("Press Enter to exit.")

