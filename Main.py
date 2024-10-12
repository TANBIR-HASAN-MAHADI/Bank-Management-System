from Admin import Admin

def user_menu(account):
    while True:
        print("\nUser Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        
        elif choice == 3:
            account.check_balance()
        
        elif choice == 4:
            account.check_transaction_history()
        
        elif choice == 5:
            amount = float(input("Enter loan amount: "))
            account.take_loan(amount)
        
        elif choice == 6:
            target_account_number = int(input("Enter target account number: "))
            if target_account_number in admin.users:
                target_account = admin.users[target_account_number]
                amount = float(input("Enter amount to transfer: "))
                account.transfer(amount, target_account)
            else:
                print("Account does not exist.")
        
        elif choice == 7:
            break

        else:
            print("Invalid choice. Please try again.")


def admin_menu(admin):
    if admin.login():  
        while True:
            print("\nAdmin Menu")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Show All Accounts")
            print("4. Check Total Bank Balance")
            print("5. Check Total Loan Amount")
            print("6. Show Users Who Have Taken Loans")
            print("7. Toggle Loan Feature")
            print("8. Exit")

            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                account_type = input("Enter account type (Savings/Current): ")
                admin.create_account(name, email, address, account_type)
            
            elif choice == 2:
                account_number = int(input("Enter account number to delete: "))
                admin.delete_account(account_number)
            
            elif choice == 3:
                admin.show_all_accounts()
            
            elif choice == 4:
                admin.check_total_balance()
            
            elif choice == 5:
                admin.check_total_loans()
            
            elif choice == 6:
                admin.show_loan_users()
            
            elif choice == 7:
                status = input("Enable loan feature? (yes/no): ").lower() == "yes"
                admin.toggle_loan_feature(status)
            
            elif choice == 8:
                break

            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to authenticate. Returning to main menu.")


admin = Admin()

while True:
    print("\nBanking System")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        admin_menu(admin)
    
    elif user_choice == 2:
        account_number = int(input("Enter your account number: "))
        if account_number in admin.users:
            user_menu(admin.users[account_number])
        else:
            print("Account does not exist.")
    
    elif user_choice == 3:
        break
    
    else:
        print("Invalid choice. Please try again.")
