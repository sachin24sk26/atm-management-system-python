from users import details, atm_pin_entry, atm_pin_change
from balance import atm_balance_inquiry, atm_cash_withdrawal, atm_cash_deposit

def atm_card_remove():
    print("Thank you for using atm services")
    print("Please remove atm card")

def atm_option():
    print("Please select an option")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Pin Change")
    option = int(input("Please select an option: "))
    if option == 1:
        atm_balance_inquiry()
    elif option == 2:
        atm_cash_withdrawal()
    elif option == 3:
        atm_cash_deposit()
    elif option == 4:
        atm_pin_change()

def atm_option_loop():
    atm_card_insert = input("Please insert atm card (enter yes to insert): ")
    if atm_card_insert.lower() == "yes":
        atm_pin_entry()
        while True:
            atm_option()
            other_option = input("Do you want to perform other option? (yes/no): ")
            if other_option.lower() == "no":
                break
        atm_card_remove()
    else:
        print("Please insert atm card")

atm_option_loop()   
