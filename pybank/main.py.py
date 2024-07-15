#just packages
import csv
from statistics import mean

# Lists to store months and profit/loss values
months = []
profits_losses = []
changes = []

# Open the CSV file in read mode
with open('Resources.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    # Read each row in the CSV file
    for row in csv_reader:
        months.append(row[0])  # Append month to the months list
        profits_losses.append(int(row[1]))  # Append profit/loss value to the profits_losses list

# Calculate total number of months
total_months = len(months)

# Calculate the net total of profit/losses
net_total = sum(profits_losses)

# Calculate changes in profit/losses
for i in range(1, len(profits_losses)):
    change = profits_losses[i] - profits_losses[i-1]  # Calculate change between current and previous month
    changes.append(change)  # Append change to the changes list

# Calculate average change in profit/losses
average_change = mean(changes)

# Determine the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_index = changes.index(greatest_increase)  # Get the index of the greatest increase
decrease_index = changes.index(greatest_decrease)  # Get the index of the greatest decrease

# Print the financial analysis
print("Financial Analysis\n")
print("-----------------------\n")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {months[increase_index + 1]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {months[decrease_index + 1]} (${greatest_decrease})")
