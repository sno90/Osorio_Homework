# import modules
import os
import csv

# set file path
bank_data_path = os.path.join('Resources',  'budget_data.csv')

# set lists
months = []
revenue = []
monthly_revenue_change = []

# open budget data file and skip header
with open(bank_data_path, newline= '') as budget: 
    csvreader = csv.reader(budget, delimiter = ',')
    header = next(csvreader)
    
# add column 1 of file to the months list
# add column 2 of file to the revenue list
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

# find total months 
#total_months = len(months)
# find total revenue by summing all the values in the revenue list
#total_revenue = sum(revenue)

# calculate monthly revenue change by looking at the 
#revenue in the next row and subtracting it by the current revenue
# add to monthly_revenue_change list
    for i in range(len(revenue)-1):
        monthly_revenue_change.append(revenue[i+1]-revenue[i])

max_revenue = max(monthly_revenue_change)
min_revenue = min(monthly_revenue_change)

max_revenue_month = monthly_revenue_change.index(max(monthly_revenue_change)) + 1
min_revenue_month = monthly_revenue_change.index(min(monthly_revenue_change)) + 1

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(revenue)}')
print(f'Average Change: ${round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}')
print(f'Greatest Increase in Profits: {months[max_revenue_month]} (${(str(max_revenue))})')
print(f'Greatest Decrease in Profits: {months[min_revenue_month]} (${(str(min_revenue))})')

output_file = os.path.join('Resources','budget_data_analysis.csv')

with open(output_file,'w') as file:
    file.write('Financial Analysis')
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write(f'Total Months: {len(months)}')
    file.write('\n')
    file.write(f'Total: ${sum(revenue)}')
    file.write('\n')
    file.write(f'Average Change: ${round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}')
    file.write('\n')
    file.write(f'Greatest Increase in Profits: {months[max_revenue_month]} (${(str(max_revenue))})')
    file.write('\n')
    file.write(f'Greatest Decrease in Profits: {months[min_revenue_month]} (${(str(min_revenue))})')