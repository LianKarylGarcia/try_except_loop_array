user_infos = {}

while True: # First loop
    try:
        while True: # Loop until the valid name is provided
            name = input("Please input name: ")
            
            if len(name) <= 5: # Setting condition for a valid name
                break # To break the inner loop if input is valid
            
            else:
                print("Input a name with 5 or fewer characters.")
                

        while True: # Loop until the valid age is provided
            age = int(input("Please input age: "))

            if age >= 18: # Setting condition for a valid age # len does not work with int 
                break # To break the inner loop if age is valid
            
            else: 
                print("Age must be 18 and above")

        user_infos[name] = { # To store user infos in the dictionary
            "name" : name,
            "age" : age
        }
        
        print(f"Name: {user_infos[name]['name']}")
        print(f"Age: {user_infos[name]['age']}")

        retry = input("Retry? Yes or no? ") # To ask user if they want to retry again

        # Setting conditions for retry
        if retry == "No":
            break # To break the outer loop  if the user says "No"
        elif retry == "Yes":
            continue # To continue the outer loop if the user says "Yes"
        else: 
            print("Invalid response. Please enter 'Yes' or 'No'")

    except ValueError:
        print("Input invalid. Please input correct values.")
        
    


