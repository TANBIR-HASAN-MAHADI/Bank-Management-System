from Account import Account

class Admin:
    def __init__(self):
        self.users = {}
        self.loan_feature_enabled = True
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.total_balance = 0

    def login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.admin_username and password == self.admin_password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password. Access denied.")
            return False

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.users[account.account_number] = account
        print(f"Account created for {name}. Account Number: {account.account_number}")

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account does not exist.")

    def show_all_accounts(self):
        if self.users:
            for acc_num, user in self.users.items():
                print(f"Account Number: {acc_num}, Name: {user.name}, Balance: {user.balance}")
        else:
            print("No accounts found.")

    def check_total_balance(self):
        print(f"Total available balance in bank: {self.total_balance}")
        return self.total_balance

    def check_total_loans(self):
        total_loans = sum(sum(user.loans) for user in self.users.values())
        print(f"Total loan amount: {total_loans}")
        return total_loans

    def show_loan_users(self):
        print("\nUsers Who Have Taken Loans:")
        has_loans = False
        for acc_num, user in self.users.items():
            if user.loans:
                total_loan_amount = sum(user.loans)
                print(f"Account Number: {acc_num}, Name: {user.name}, Loans Taken: {len(user.loans)}, Total Loan Amount: {total_loan_amount}")
                for idx, loan in enumerate(user.loans, 1):
                    print(f"  Loan {idx}: {loan}")
                has_loans = True
        if not has_loans:
            print("No users have taken loans yet.")

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status
        for user in self.users.values():
            user.loan_enabled = status
        state = "enabled" if status else "disabled"
        print(f"Loan feature {state}.")

