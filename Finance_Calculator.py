import math

def main():
    # Display options to the user
    print("  ")
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("  ")
    print("investment       - to calculate the amount of interest you'll earn on your investment")
    print("  ")
    print("bond             - to calculate the amount you'll have to pay on a home loan")

    # Get the user's choice
    choice = input().lower()

    if choice == 'investment':
        # Get investment details from the user
        principal = float(input("Enter the amount of money you are depositing: "))
        rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years you plan on investing for: "))
        interest_type = input("Do you want 'simple' or 'compound' interest? ").lower()

        if interest_type == 'simple':
            # Calculate simple interest
            amount = principal * (1 + rate * years)
        elif interest_type == 'compound':
            # Calculate compound interest
            amount = principal * math.pow((1 + rate), years)
        else:
            print("Invalid interest type. Please enter either 'simple' or 'compound'.")
            return
        
        print(f"The total amount after {years} years is: {amount}")

    elif choice == 'bond':
        # Get bond details from the user
        present_value = float(input("Enter the present value of the house: "))
        annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
        months = int(input("Enter the number of months you plan to take to repay the bond: "))

        # Calculate monthly interest rate
        monthly_rate = annual_rate / 12

        # Calculate monthly repayment
        repayment = (monthly_rate * present_value) / (1 - math.pow((1 + monthly_rate), -months))
        print(f"The monthly repayment amount is: {repayment}")

    else:
        print("Invalid input. Please enter either 'investment' or 'bond'.")

if __name__ == "__main__":
    main()