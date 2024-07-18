branch_list = []
loan_list = []
account_list = []
customer_list = []
def branch():
    branch_id = int(input("enter branch_id (eg., 1): "))
    name = input("enter name (eg., HBL): ")
    branch_address = input("enter branch address (eg., street 01, attock): ")
    branch_list.insert(0, branch_id)
    branch_list.insert(1, name)
    branch_list.insert(2, branch_address)


def loan():
    loan_id = int(input("enter loan_id (eg., 1): "))
    loan_type = input("enter loan type (eg., annual or monthly): ")
    amount = int(input("enter loan amount: "))
    loan_list.insert(0, loan_id)
    loan_list.insert(1, loan_type)
    loan_list.insert(2, amount)



def account():
    account_no = int(input("enter account no: "))
    acc_type = input("enter account type (eg., personal): ")
    balance = int(input("enter the balance of the account: "))
    account_list.insert(0, account_no)
    account_list.insert(1, acc_type)
    account_list.insert(2, balance)


def customer():
    cus_id = int(input("enter customer id (eg., 1): "))
    address = input("enter your home address: ")
    name = input("enter your name (eg., laiba): ")
    phone = int(input("enter phone number (eg., 0314 123 3213"))
    customer_list.insert(0, cus_id)
    customer_list.insert(1, address)
    customer_list.insert(2, name)
    customer_list.insert(3, phone)


print("\nBranch:")
branch()
print("\nLoan:")
loan()
print("\nAccount:")
account()
print("\nCustomer:")
customer()

print(" ")
print(branch_list)
print(loan_list)
print(account_list)
print(customer_list)

