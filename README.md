# AdventureWorks2019 Sales Analysis Project

## Overview
This project analyses sales performance, store operations, and employee metrics using the AdventureWorks2019 database. The analysis focuses on identifying key relationships between various business metrics to provide actionable insights for business growth.

## Key Questions Addressed
- Regional sales performance analysis
- Employee leave and bonus correlations
- Country-revenue relationships
- Sick leave patterns across job titles
- Store trading duration impact on revenue
- Store size, employee, and revenue relationships

## Tools & Technologies Used
- SQL (for data extraction)
- Python
  - Pandas (data manipulation)
  - Matplotlib/Seaborn (visualisation)
- AdventureWorks2019 Database

## Key Findings
- The US dominates sales, with the Southwest region leading at 34% market share.
- Store performance strongly correlates with:
  - Trading duration
  - Store size
  - Product diversity
- Weak correlation (0.38) between annual leave and bonuses.
- The majority of stores are under 1-year old.

## How to Run
1. Restore the AdventureWorks2019 database.
2. Download CSV files in `datasets`.
3. Run Python analysis scripts.
4. View generated visualisations.

## Dependencies
- Python 3.x
- SQL Server
- Required Python packages:
  - pandas
  - matplotlib
  - seaborn
