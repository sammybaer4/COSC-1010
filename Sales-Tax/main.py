#
# Sam Baer
# 2/03/2026
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
purchase = 0.0
stateTax = 0.0
sountyTax= 0.0
totalTax = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the amount of the purchase.
purchase = float(input("Enter the amount of purchase: "))

# Calculate the state sales tax.
stateTax = purchase * STATE_TAX_RATE

#Calculate the county sales tax.
CountyTax = purchase * COUNTY_TAX_RATE

# Calculate the total tax
TotalTax = stateTax + CountyTax

# Calculate the total of the sale
TotalSale = purchase + TotalTax

# Print information about the sale.
print("Purchase Amount:", format(purchase, '.2f'))
print("StateTax:", format(stateTax, '.2f'))
print("CountyTax:", format(CountyTax, '.2f'))
print("TotalTax:", format(TotalTax, '.2f'))
print("SaleTotal:", format(TotalSale, '.2f'))
