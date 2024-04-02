while True:
  try:
      print("Bill Split")

      # Input for total bill
      print("How much is your bill?")
      bill_total = float(input())

      # Input for number of people sharing
      print("How many people are splitting?")
      people = int(input())

      # Input for tip percentage
      print("Are you leaving a tip?")
      tip_percentage = float(input())

      break  # Break the loop if inputs are valid
  except ValueError:
      print("That's not a number, silly! Try again!")

# Calculate tip, bill total, and cost per person
percentage_decimal = tip_percentage / 100
tip_total = bill_total * percentage_decimal
bill_total = bill_total + tip_total
cost_per_person = bill_total / people

# Round to two decimal places
bill_total = round(bill_total, 2)
cost_per_person = round(cost_per_person, 2)

# Display the results
print(f"Total bill including tip is £{bill_total}")
print(f"Total cost per person is £{cost_per_person}")
