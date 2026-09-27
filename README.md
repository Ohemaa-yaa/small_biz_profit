# Small Business Profit Calculator
A simple Python library for calculating profit and profit margin for small businesses.

# Features
The library currently calculates:
. Gross Profit
. Net Profit
. Profit Margin

# How It Works
The library uses three main business inputs:

.Revenue - the total income from sales.
.Cost of Goods - the cost of producing or purchasing the goods sold.
.Expenses - other business operating expenses.

# Formulas

# Gross Profit
Gross Profit = Revenue - Cost of Goods

# Net Profit
Net Profit = Gross Profit - Expenses

# Profit Margin
Profit Margin = (Net Profit / Revenue) * 100

# Installation
Clone the repository:

git clone
https://github.com/Ohemaa-yaa/small_biz_profit.git .


Navigate into the project:
cd "Small Business Profit Calculator"

# Usage
Import the ProfitCalculator class:

 from small_business_profit import
 ProfitCalculator

 business = ProfitCalculator(
        revenue = 25000,
    cost_of_goods = 19000,
    expenses = 3000
)

print("Gross Profit:", business.gross_profit())
print("Net Profit:", business.net_profit())
print("Profit Margin:", business.profit_margin(),
"%")
 
# Example Output
Gross Profit: 6000
Net Profit: 3000
Profit Margin: 12.0%

# Project Structure
Small_Business_Profit_Calculator/
|
|---Small_Business_Profit/
|   |--__init__.py
|   |___calculator.py
|
|---Examples/
|   |__basic_example.py
|
|__README.md

# Purpose
Small Business Profit Calculator is designed as a simple tool to help small businesses understand their basic profitability using straightforward financial calculations.

# License
This project is created is created for educational purposes.
