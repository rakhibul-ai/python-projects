rent = float(input("Enter the rent: "))
food = float(input("Enter the food cost: "))
electricity_unit = float(input("Enter the electricity unit: "))
unit_cost = float(input("Enter per unit cost: "))
persons = int(input("Enter total persons: "))

if persons <= 0:
    print("Number of persons must be greater than zero.")
else:
    electricity_cost = electricity_unit * unit_cost
    total_cost = rent + food + electricity_cost
    person_cost = total_cost / persons
    print(f"Each person should pay: {person_cost:.2f}")
