food_charge = float(input('Enter the cost of the meal: $'))

tip = food_charge * 0.18
tax = food_charge * 0.07

print('Food charge: ${:.2f}'.format(food_charge))
print('Tip: ${:.2f}'.format(tip))
print('Tax: ${:.2f}'.format(tax))
print('Total cost: ${:.2f}'.format(food_charge+tip + tax))
