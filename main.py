while True:
  try:
      print("Bill Split")

      # Input for total bill with a maximum of 2 decimal places
      print("What is the total bill? (up to 2 decimal places)")
      while True:
          bill_total = input()
          try:
              if '.' in bill_total:
                  integer_part, decimal_part = bill_total.split('.')
                  if len(decimal_part) <= 2:
                      bill_total = '{:.2f}'.format(float(bill_total))  # Format to 2 decimal places
                      break
                  else:
                      print("Please enter a valid number with up to 2 decimal places.")
              else:
                  bill_total = '{:.2f}'.format(float(bill_total))  # Format to 2 decimal places
                  break
          except ValueError:
              print("Invalid input. Please enter a valid number with up to 2 decimal places.")

      # Input for number of people sharing
      print("How many people are sharing?")
      people = int(input())
      print()

      # Input for tip percentage
      print("What percentage tip would you like to leave?")
      tip_percentage = float(input("Enter tip percentage (%): "))
      print()

      # Calculate tip, bill total, and cost per person
      percentage_decimal = tip_percentage / 100
      tip_total = float(bill_total) * percentage_decimal
      bill_total = float(bill_total) + tip_total
      cost_per_person = bill_total / people

      # Round to two decimal places
      bill_total = round(bill_total, 2)
      cost_per_person = round(cost_per_person, 2)

      # Display the results
      print(f"Total bill including tip is £{bill_total}")
      print(f"Total cost per person is £{cost_per_person}")
      print()

      # Ask if the user wants to split another bill
      choice = input("Split another bill? (Yes/No): ")
      if choice.lower() != 'yes':
          break

  except ValueError:
      print("Invalid input. Please enter a valid number.")
