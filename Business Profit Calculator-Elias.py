'''Business Profit Calculator
Calculates profit and margin percentage
from revenue and cost data'''

# Get revenue from business/user
revenue = float(input("Enter total revenue: $"))

# Get costs from business/user  
costs = float(input("Enter total costs: $"))

# Calculate net profit
profit = revenue - costs

# Calculate profit margin percentage
margin = (profit / revenue) * 100

# Display results
print("\n--- Financial Summary ---")
print("Revenue: $" + str(revenue))
print("Costs: $" + str(costs))
print("Profit: $" + str(profit))
print("Profit Margin: " + str(margin) + "%")