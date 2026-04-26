from users import details

def atm_balance_inquiry():
    print("-----Balance inquiry-----")
    print("Balance: ", details["Balance"])
    return True

def atm_cash_withdrawal():
    print("-----Withdraw cash-----")
    amount = int(input("Enter withdrawal amount: "))
    if amount > details["Balance"]:
        print("Insufficient balance")
        return False
    else:
        details["Balance"] -= amount
        print("Withdrawal successful")
        return True

def atm_cash_deposit():
    print("-----Cash deposit-----")
    amount = int(input("Enter deposit amount: "))
    details["Balance"] += amount
    print("Deposit successful")
    return True
