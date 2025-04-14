import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Question 1 

# Chart 1
highest_sales = pd.read_csv('./datasets/highest_sales.csv')
regional_sales = pd.read_csv('./datasets/regional_sales.csv')

# Sales by country 
plt.figure(figsize=(10, 6))
plt.bar(
    x=highest_sales['CountryRegionCode'],              
    height=highest_sales['country_sales'],      
    width=0.6,
    bottom=0,
    align='center',
    color='lightcoral',
    edgecolor='black')

plt.title("Sales by Country")
plt.xlabel("Country")  
plt.ylabel("Total Revenue")  
plt.tight_layout()
plt.show()

#heatmap
heatmap_data = regional_sales.set_index('Region')['RegionalSales'].to_frame()
heatmap_data = heatmap_data.reset_index()

heatmap_data.columns = ['Region', 'Sales']   # Rename columns for clarity

plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data.set_index('Region'), annot=True, cmap="YlOrRd", fmt='.1f', cbar_kws={'label': 'Sales'})

plt.title('Heatmap of Regional Sales in the US')
plt.ylabel('Region')
plt.tight_layout()
plt.show()


# Pie Chart for Regional Sales
plt.figure(figsize=(10, 8))
plt.pie(regional_sales['RegionalSales'], labels=regional_sales['Region'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3"))

plt.title('Regional Sales Distribution in the US')
plt.axis('equal')  
plt.tight_layout()
plt.show()


# Question 2
hours_bonus = pd.read_csv('./datasets/vacation_hours_bonus.csv')

# Calculate the correlation
correlation = hours_bonus['VacationHours'].corr(hours_bonus['Bonus'])
print("Correlation between VacationHours and Bonus: " + str(correlation))

# regression line plot
sns.regplot(data=hours_bonus, x='VacationHours', y='Bonus')
plt.title('Regression Plot: Vacation Hours vs Bonus')
plt.xlabel('Vacation Hours')
plt.ylabel('Bonus')
plt.show()

# Question 3
country_revenue = pd.read_csv('./datasets/country_revenue.csv')

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


# Question 4
sick_leave = pd.read_csv('./datasets/sick_leave_job.csv')

grouped = sick_leave.groupby('JobTitle')['SickLeaveHours'].mean()
print(grouped)

# Sort the grouped data by 'sick_leave_hours' in ascending order
grouped_sorted = grouped.sort_values(ascending=True)

print(grouped_sorted)

# Plotting
plt.figure(figsize=(8, 12))
plt.barh(grouped_sorted.index, grouped_sorted.values)
plt.xlabel('Average Sick Leave Hours')
plt.ylabel('Job Title')
plt.title('Average Sick Leave Hours by Job Title')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
sns.boxplot(x='SickLeaveHours', y='JobTitle', data=sick_leave, order=sick_leave.groupby('JobTitle')['SickLeaveHours'].mean().sort_values().index)
plt.title('Distribution of Sick Leave Hours by Job Title')
plt.xlabel('Sick Leave Hours')
plt.ylabel('Job Title')
plt.grid(True)
plt.tight_layout()
plt.show()

# Question 5
df = pd.read_csv('./datasets/duration_revenue.csv')  

# seaborn style
sns.set_style("whitegrid")  
sns.set_palette("husl")  

# Calculate average revenue by category
avg_revenue = df.groupby('TradingDurationCategory')['TotalRevenue'].mean().sort_values()

# 1. Bar Plot: Average Revenue by Trading Duration Category
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_revenue.index, y=avg_revenue.values)
plt.title('Average Revenue by Trading Duration')
plt.xlabel('Trading Duration')
plt.ylabel('Average Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()


# 2. Bar Plot: Number of Stores in Each Category
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='TradingDurationCategory')
plt.title('Number of Stores by Trading Duration')
plt.xlabel('Trading Duration')
plt.ylabel('Number of Stores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Question 6
df = pd.read_csv('./datasets/size_employee_rev.csv')  

# style
sns.set_style("whitegrid")

# Bar Plot: Average Revenue by Store Size
plt.figure(figsize=(12, 6))
avg_revenue = df.groupby('StoreSizeByRevenue')['TotalRevenue'].mean().sort_values()
sns.barplot(x=avg_revenue.index, y=avg_revenue.values)
plt.title('Average Revenue by Store Size', fontsize=14, pad=20)
plt.xlabel('Store Size Category', fontsize=12)
plt.ylabel('Average Revenue (USD)', fontsize=12)
plt.xticks(rotation=45)
# Add value labels on bars
for i, v in enumerate(avg_revenue.values):
    plt.text(i, v, f'${v:,.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Scatter Plot: Number of Unique Products vs Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='NumberOfUniqueProducts', y='TotalRevenue', 
                hue='StoreSizeByRevenue', alpha=0.6)
plt.title('Relationship between Number of Products and Revenue', fontsize=14)
plt.xlabel('Number of Unique Products', fontsize=12)
plt.ylabel('Total Revenue (USD)', fontsize=12)
plt.tight_layout()
# plt.show()



