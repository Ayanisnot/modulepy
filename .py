age_input = input("enter your age :")

if age_input.isdigit():
    age = int(age_input)

    if age <= 0:
     print("Error: Age must a positive number.")

    else:
     print("age is valid.")


    if age % 2 == 0:
      print("You age is even.")
    else:
      print("Your age is odd.")


else:
  print("Invalid input. Please enter a number")

    
