import csv
import os

# Define the path to the dataset
file_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = net_total = 0
changes = []
greatest_increase = ["", float("-inf")]
greatest_decrease = ["", float("inf")]

# Open and read the CSV file
try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        for row in reader:
            # Check if the row is not empty
            if row:
                # Directly access the date and profit/loss values from the row
                date, profit_loss = row
                profit_loss = int(profit_loss.replace(',', ''))  # Remove commas when present
                
                # Increment the total number of months and net total
                total_months += 1
                net_total += profit_loss
                
                # Calculate  change in "Profit/Losses"
                if total_months > 1:
                    change = profit_loss - prev_profit_loss
                    changes.append(change)
                    
                    # Update the greatest increase/decrease
                    if change > greatest_increase[1]:
                        greatest_increase = [date, change]
                    if change < greatest_decrease[1]:
                        greatest_decrease = [date, change]
                
                # Update the previous profit/loss
                prev_profit_loss = profit_loss
            else:
                print("Warning: Skipping an empty row.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Calculate the average change and output the results
if total_months > 0:
    average_change = sum(changes) / len(changes) if changes else 0
    results = f"""Financial Analysis
    ------------------
    Total Months: {total_months}
    Total: ${net_total}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
    Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"""
    print(results)
    with open ('financial_stats.txt', 'w') as output_file:
        output_file.write(results)
else:
    print("No data to analyze.")

