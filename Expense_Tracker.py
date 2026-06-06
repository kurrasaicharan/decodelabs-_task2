# Expense Tracker Project

# Developed by Sai Charan



print("===================================")

print("      EXPENSE TRACKER SYSTEM")

print("===================================")



# Variables

total_expense = 0

expense_count = 0



# User choice loop

while True:



    print("\n1. Add Expense")

    print("2. View Total Expense")

    print("3. Exit")



    choice = input("Enter your choice: ")



    # Add Expense

    if choice == "1":

        expense = float(input("Enter expense amount: ₹"))



        total_expense = total_expense + expense

        expense_count += 1



        print("Expense Added Successfully!")



    # View Total

    elif choice == "2":

        print("\n====== Expense Summary ======")

        print("Number of Expenses :", expense_count)

        print("Total Expense      : ₹", total_expense)



        # Average calculation

        if expense_count > 0:

            average = total_expense / expense_count

            print("Average Expense    : ₹", round(average, 2))

        else:

            print("No expenses added yet.")



    # Exit

    elif choice == "3":

        print("\nThank You for using Expense Tracker!")

        print("Program Closed Successfully.")

        break



    # Invalid Choice

    else:

        print("Invalid Choice! Please try again.")