details = {
    "name": "Sachin",
    "PIN": 1234,
    "Balance": 50000
}

def atm_pin_change():
    print("-----Pin change-----")
    old_pin = int(input("Enter old pin: "))
    if old_pin == details["PIN"]:
        print("Pin correct")
        new_pin = int(input("Enter new pin: "))
        details["PIN"] = new_pin
        print("Pin changed successfully")
        return True
    else:
        print("Incorrect pin")
        return False

def atm_pin_entry():
    atm_pin = int(input("Enter pin: "))
    if atm_pin == details["PIN"]:
        print("Please enter your option")
        return True
    else:
        print("Incorrect pin")
        return False
