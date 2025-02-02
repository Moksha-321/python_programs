principal_amount = int(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))
rate_of_interest = int(input("Enter the rate of interests: "))
si = (principal_amount*years*rate_of_interest)/100
print(f"SI: {si}")
ci = (principal_amount*(1+(rate_of_interest/100)))**years
print(f"CI: {ci}")
