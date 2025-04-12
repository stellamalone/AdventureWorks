import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import geopandas as gpd
import os 


plt.title("Sales Over Time by Country")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.legend(title='Country')
plt.grid(True)
plt.tight_layout()
plt.show()

# Load the CSV file
highest_sales = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/highest_sales.csv')
regional_sales = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/regional_sales.csv')

heatmap_data = regional_sales.set_index('Region')['RegionalSales'].to_frame()

# Reset index to make 'Region' a column again for plotting
heatmap_data = heatmap_data.reset_index()

# Rename columns for clarity
heatmap_data.columns = ['Region', 'Sales']

plt.figure(figsize=(10, 8))
# heatmap
sns.heatmap(heatmap_data.set_index('Region'), annot=True, cmap="YlOrRd", fmt='.1f', cbar_kws={'label': 'Sales'})

plt.title('Heatmap of Regional Sales in the US')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

# histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=regional_sales, x='RegionalSales', bins=20, kde=False, color='lightcoral', edgecolor='black')

plt.title("Distribution of Regional Sales in the Best Performing Country (US)")
plt.xlabel("Regional Sales")
plt.ylabel("Frequency")
plt.tight_layout()
# plt.show()

# Pie Chart for Regional Sales
# plt.figure(figsize=(10, 8))
# plt.pie(regional_sales['RegionalSales'], labels=regional_sales['Region'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3"))

# plt.title('Regional Sales Distribution in the US')
# plt.axis('equal')  
# plt.tight_layout()
# plt.show()

# print(highest_sales.head)  # To see the first few rows of data
# print(regional_sales.head)

# plt.figure(figsize=(10, 6))
# plt.bar(
#     x=highest_sales['CountryRegionCode'],              
#     height=highest_sales['country_sales'],      
#     width=0.6,
#     bottom=0,
#     align='center',
#     color='lightcoral',
#     edgecolor='black')

# plt.title("Sales by Country")
# plt.xlabel("Country")  
# plt.ylabel("Total Revenue")  
# plt.tight_layout()
# plt.show()


# plt.bar(
#     x=regional_sales['Region'],              
#     height=regional_sales['RegionalSales'],      
#     width=0.6,
#     bottom=0,
#     align='center',
#     color='lightcoral',
#     edgecolor='black')
# plt.title("Best Performing Region")
# plt.xlabel("Total Revenue")
# plt.ylabel("Region")
# plt.show()

plt.figure(figsize=(7, 8))
plt.barh(regional_sales['Region'], regional_sales['RegionalSales'])
plt.xlabel('Regional Sales')
plt.ylabel('Region')
plt.title('Regional Sales in Best Performing country (US)')
plt.tight_layout()
# plt.show()

# Sort the DataFrame by 'RegionalSales' in descending order
regional_sales_sorted = regional_sales.sort_values(by='RegionalSales', ascending=False)

# Create the plot
plt.figure(figsize=(7, 8))
plt.barh(regional_sales_sorted['Region'], regional_sales_sorted['RegionalSales'])

# Customize the plot
plt.xlabel('Regional Sales')
plt.ylabel('Region')
plt.title('Regional Sales in Best Performing country (US)')

# Show the plot
plt.tight_layout()
plt.show()


# Load the CSV file
hours_bonus = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/vacation_hours_bonus.csv')

# Calculate the correlation
correlation = hours_bonus['VacationHours'].corr(hours_bonus['Bonus'])
# print("Correlation between VacationHours and Bonus: " + str(correlation))

# Visualize the relationship
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=hours_bonus, x='VacationHours', y='Bonus')
# plt.title('Relationship between Vacation Hours and Bonus')
# plt.xlabel('Vacation Hours')
# plt.ylabel('Bonus')
# plt.show()

# Optionally, you might want to look at a regression line
# sns.regplot(data=hours_bonus, x='VacationHours', y='Bonus')
# plt.title('Regression Plot: Vacation Hours vs Bonus')
# plt.xlabel('Vacation Hours')
# plt.ylabel('Bonus')
# plt.show()

country_revenue = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/country_revenue.csv')

plt.bar(
    x=country_revenue['CountryRegionCode'],              
    height=country_revenue['TotalRevenue'],      
    width=0.6,
    bottom=0,
    align='center',
    color='lightcoral',
    edgecolor='black')
plt.title("Country and Revenue Relationship")
plt.xlabel("Country Region Code")
plt.ylabel("TotalRevenue")
# plt.show()

sick_leave = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/sick_leave_job.csv')

grouped = sick_leave.groupby('JobTitle')['SickLeaveHours'].mean()
# print(grouped)

# Sort the grouped data by 'sick_leave_hours' in ascending order
grouped_sorted = grouped.sort_values(ascending=True)

# print(grouped_sorted)

# # Plotting
# plt.figure(figsize=(8, 12))
# plt.barh(grouped_sorted.index, grouped_sorted.values)
# plt.xlabel('Average Sick Leave Hours')
# plt.ylabel('Job Title')
# plt.title('Average Sick Leave Hours by Job Title')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(15, 10))
sns.boxplot(x='SickLeaveHours', y='JobTitle', data=sick_leave, order=sick_leave.groupby('JobTitle')['SickLeaveHours'].mean().sort_values().index)
plt.title('Distribution of Sick Leave Hours by Job Title')
plt.xlabel('Sick Leave Hours')
plt.ylabel('Job Title')
plt.grid(True)
plt.tight_layout()
# plt.show()


# Load the CSV file
df = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/tradingDuration_revenue.csv')

# Calculate correlation
correlation = df['TradingDuration'].corr(df['AnnualRevenue'])
print(f"Correlation between Trading Duration and Annual Revenue: {correlation}")

# Visualize the relationship
plt.figure(figsize=(10, 6))
plt.scatter(df['TradingDuration'], df['AnnualRevenue'])
plt.xlabel('Trading Duration (Years)')
plt.ylabel('Annual Revenue')
plt.title('Relationship between Store Trading Duration and Annual Revenue')
# plt.show()


# Load the data from CSV
data = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/size_employees_rev.csv')

# Compute correlation matrix
correlation_matrix = data[['StoreSize', 'NumberOfEmployees', 'TotalRevenue']].corr()

# Visualize the correlation matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
# plt.title('Correlation Heatmap of Store Size, Number of Employees, and Total Revenue')
# plt.show()

# Scatter plots for visual inspection
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.scatter(data['StoreSize'], data['TotalRevenue'])
plt.xlabel('Store Size')
plt.ylabel('Total Revenue')
plt.title('Store Size vs Total Revenue')

plt.subplot(1, 2, 2)
plt.scatter(data['NumberOfEmployees'], data['TotalRevenue'])
plt.xlabel('Number of Employees')
plt.ylabel('Total Revenue')
plt.title('Number of Employees vs Total Revenue')
plt.tight_layout()
# plt.show()



# Step 1: Read the CSV file
df = pd.read_csv('/Users/stellamalone/Downloads/dataworks_project/question1.csv')

# Step 2: Group by 'CountryRegionCode' and sum the sales
grouped_data = df.groupby('CountryRegionCode').agg({
    'SalesLastYear': 'sum',
    'SalesYTD': 'sum'
}).reset_index()

# Step 3: Set up the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Step 4: Define the width of the bars
bar_width = 0.35

# Step 5: Create the bar positions
r1 = range(len(grouped_data))
r2 = [x + bar_width for x in r1]

# Step 6: Plot the bars
ax.bar(r1, grouped_data['SalesLastYear'], color='skyblue', width=bar_width, label='Sales Last Year')
ax.bar(r2, grouped_data['SalesYTD'], color='orange', width=bar_width, label='Sales YTD')

# Step 7: Customize the plot
ax.set_xlabel('Country/Region Code', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_title('Sales Comparison by Country/Region', fontsize=14)
ax.set_xticks([r + bar_width/2 for r in range(len(grouped_data))])
ax.set_xticklabels(grouped_data['CountryRegionCode'], rotation=45, ha='right')

# Step 8: Add a legend
ax.legend()

# Step 9: Adjust layout and display the plot
plt.tight_layout()
plt.show()
