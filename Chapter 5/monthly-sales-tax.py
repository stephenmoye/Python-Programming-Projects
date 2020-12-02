# 9. Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales for the month, and
# the amount of state and county sales tax collected. The state sales tax rate is 5 percent and the
# county sales tax rate is 2.5 percent. Write a program that asks the user to enter the total sales for
# the month. From this figure, the application should calculate and display the following:
# The amount of county sales tax
# The amount of state sales tax
# The total sales tax (county plus state)

COUNTY_TAX = .025
STATE_TAX =  .05

def main():
    sales = get_sales()
    tax(COUNTY_TAX, STATE_TAX, sales)

def get_sales():
    monthlySales = float(input("Enter your total monthly sales "))
    return monthlySales

def tax(county, state, sales):
  countyTax = sales * county
  stateTax = sales * state
  totalTax(countyTax, stateTax)

def totalTax(county, state):
    print("County Tax: ", county)
    print("State Tax: ", state)
    print("Grand Total: ", state + county)

main()
