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
        
        break # To break the outer loop if both inputs are valid

    except ValueError:
        print("Input invalid. Please input correct values.")

