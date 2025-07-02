# A program to determine the weight of a person
name = input("Enter your name: ")
if not name.strip():
    print("Name cannot be empty. Please enter a valid name.")
    name = input("Enter your name: ")


while True:
    try:
        weight = float(input("Please enter your weight: "))
        if weight <= 0:
            print("Invalid weight. Please enter a positive number.")
            continue
        if weight > 1000:
            print("Invalid weight. Please enter a realistic weight (less than 1000).")
            continue
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        break

    while True:
        unit = input("Is this in pounds or kilograms? (p/k): ")
        if unit.lower() not in ['p', 'k']:
            print("Invalid unit. Please enter 'p' for pounds or 'k' for kilograms.")
            continue

        if unit.lower() == 'p':
            weight = weight * 0.453592  # Convert pounds to kilograms
            print(f"{name}, your weight in kilograms is {weight:.2f} kg.")
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
      
    continue_choice = input("Do you want to check another weight? (yes/no): ").strip().lower()

    if continue_choice == 'yes':
       
        user_type = input("New user? (yes/no): ").strip().lower()
        if user_type == 'yes':
           
            name = input("Enter your name: ")
        else:
            # Keep existing name
            print(f"Welcome back {name}!")
        
    else:
        
        break
                
input("Press Enter to exit.")


    




  