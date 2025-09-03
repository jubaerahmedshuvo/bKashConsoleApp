import os
from queue import PriorityQueue

def send_money():
    account = int(input("Enter receiver bKash Account number: "))
    print("Your chosen Number: ", account)
    amt = int(input("Enter Amount: "))
    print("Amount: ", amt)
    reference = input("Enter Reference: ")
    print("Reference: ", reference)
    pin = input("Enter Menu Pin to Confirm: ")
    print("Money Sent Successfully!")
    print(f"BDT {amt} has been sent to {account} with '{reference}'.")

def biller_send():
    while True:
        print("1. Biller")
        print("0. Menu")
        sub_choice = input("Enter your Choice: ")
        if sub_choice == "1":
            send_money()
        elif sub_choice == "0":
            list_operations()

#----------Main Menu_______________
print("bkash")
def list_operations():
    while True:
        print("1. Send Money")
        print("2. Send Money to Non-bkash User")
        print("3. Mobile Recharge")
        print("4. Payment")
        print("5. Cash Out")
        print("6. Pay Bill")
        print("7. My bkash")
        print("8. Reset Pin")
        print("0. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            account = int(input("Enter receiver bKash Account number: "))
            print("Your chosen Number: ", account)
            amt = int(input("Enter Amount: "))
            print("Amount: ", amt)
            reference = input("Enter Reference: ")
            print("Reference: ", reference)
            pin = input("Enter Menu Pin to Confirm: ")
            print("Money Sent Successfully!")
            print(f"BDT {amt} has been sent to {account} with '{reference}'.")
        elif choice == "2":
            account = int(input("Enter receiver number: "))
            print("Your chosen Number: ", account)
            amt = int(input("Enter Amount: "))
            print("Amount: ", amt)
            reference = input("Enter Reference: ")
            print("Reference: ", reference)
            pin = input("Enter Menu Pin to Confirm: ")
            print("Money Sent Successfully!")
            print(f"BDT {amt} has been sent to {account} with '{reference}'.")
        elif choice == "3":
            print("bkash")
            while True:
                print("1. Robi")
                print("2. Airtel")
                print("3. Banglalink")
                print("4. GrameenPhone")
                print("5. Teletalk")
                print("0. Back to Main Menu")
                sub_choice = input("Enter your Choice: ")
                if sub_choice == "1":
                    num=int(input("Enter Robi Number: "))
                    print("Your chosen Number: ", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Money Sent Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "2":
                    num = input("Enter Airtel Number: ")
                    print("Your chosen Number:", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Money Sent Successfully!")
                    print(f"BDT {amt} has been sent to {num} .")
                elif sub_choice == "3":
                    num = input("Enter Banglalink Number: ")
                    print("Your chosen Number:", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Money Sent Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "4":
                    num = input("Enter GrameenPhone Number: ")
                    print("Your chosen Number:", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Money Sent Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "5":
                    num = input("Enter Teletalk Number: ")
                    print("Your chosen Number:", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Money Sent Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "0":
                    break  # <-- This takes you back to main menu
                else:
                    print("Invalid choice, try again!")

        elif choice == "4":
            account = int(input("Enter Marchent Account number: "))
            print("Your chosen Number: ", account)
            amt = int(input("Enter Amount: "))
            print("Amount: ", amt)
            reference = input("Enter Reference: ")
            print("Reference: ", reference)
            pin = input("Enter Menu Pin to Confirm: ")
            print("Your Payment is Successfully!")
            print(f"BDT {amt} has been sent to {account} with '{reference}'.")
        elif choice == "5":
            print("bKash")
            while True:
                print("1. From Agent")
                print("2. From ATM")
                print("3. Priyo Agent Numbers")
                print("4. Setup to 2 Priyo Agent Numbers to Cash Out at 1.49%")
                print("5. Special Cash Out Charge and Balance")
                print("0. Back to Main Menu")
                sub_choice = input("Enter your Choice: ")
                if sub_choice == "1":
                    num = int(input("Enter Agent Number: "))
                    print("Your Agent Number: ", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Cash Out Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "2":
                    num = input("Enter menu oin to request ATM Cash Out: ")
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Cash Out Successfully!")
                elif sub_choice == "3":
                    num = int(input("Enter Priyo Agent Number: "))
                    print("Your Agent Number: ", num)
                    amt = int(input("Enter Amount: "))
                    print("Amount: ", amt)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Cash Out Successfully!")
                    print(f"BDT {amt} has been sent to {num}.")
                elif sub_choice == "4":
                    num = input("Enter Your Agent Number: ")
                    print("Your chosen Number:", num)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Priyo Agent Number added Successfully!")
                elif sub_choice == "5":
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Balance for Special Cash Out charge/thousand: 7TK(ATM Only)")  # Question: From here add sub_choice to return to main menu again
                elif sub_choice == "0":
                    break  # <-- This takes you back to main menu
                else:
                    print("Invalid choice, try again!")
        elif choice == "6":
            print("bKash")
            while True:
                print("1. Electricity(Prepaid)")
                print("2. Electricity(Postpaid)")
                print("3. Gas")
                print("4. Water")
                print("5. Internet and Phone")
                print("6. TV")
                print("7. City Service")
                print("8. Education")
                print("9. Financial Services")
                print("0. Back to Main Menu")
                sub_choice = input("Enter your Choice: ")
                if sub_choice == "1":
                    print("bkash")
                    while True:
                        print("1. DESCO")
                        print("2. Pollibydut")
                        print("0. Back to Main Menu")
                        sub_choice = input("Enter your Choice: ")
                        if sub_choice == "1":
                            Enum = int(input("Enter Your Electricity account Number: "))
                            print("Your Electricity Account Number: ", Enum)
                            due = int(input("Enter Your Due: "))
                            print("Your Due Amount: ", due)
                            pin = input("Enter Menu Pin to Confirm: ")
                            print("Payment Successfully and Download the receipt")
                        elif sub_choice == "2":
                            Enum = int(input("Enter Your Electricity account Number: "))
                            print("Your Electricity Account Number: ", Enum)
                            due = int(input("Enter Your Due: "))
                            print("Your Due Amount: ", due)
                            pin = input("Enter Menu Pin to Confirm: ")
                            print("Payment Successfully and Download the receipt")
                        elif sub_choice == "0":
                            break  # <-- This takes you back to menu
                        else:
                            print("Invalid choice, try again!")
                elif sub_choice == "2":
                    print("bKash")
                    while True:
                        print("1. DESCO")
                        print("2. Pollibydut")
                        print("0. Back to Main Menu")
                        sub_choice = input("Enter your Choice: ")
                        if sub_choice == "1":
                            Enum = int(input("Enter Your Electricity account Number: "))
                            print("Your Electricity Account Number: ", Enum)
                            due = int(input("Enter Your Due: "))
                            print("Your Due Amount: ", due)
                            pin = input("Enter Menu Pin to Confirm: ")
                            print("Payment Successfully and Download the receipt")
                        elif sub_choice == "2":
                            Enum = int(input("Enter Your Electricity account Number: "))
                            print("Your Electricity Account Number: ", Enum)
                            due = int(input("Enter Your Due: "))
                            print("Your Due Amount: ", due)
                            pin = input("Enter Menu Pin to Confirm: ")
                            print("Payment Successfully and Download the receipt")
                        elif sub_choice == "0":
                            break  # <-- This takes you back to menu
                        else:
                            print("Invalid choice, try again!")
                elif sub_choice == "3":
                    Gnum = int(input("Enter Your Electricity account Number: "))
                    print("Your Electricity Account Number: ", Gnum)
                    due = int(input("Enter Your Due: "))
                    print("Your Due Amount: ", due)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Payment Successfully and Download the receipt")
                    print(f"BDT {due} has been sent to {Gnum}.")
                elif sub_choice == "4":
                    Wnum = int(input("Enter Your Electricity account Number: "))
                    print("Your Electricity Account Number: ", Wnum)
                    due = int(input("Enter Your Due: "))
                    print("Your Due Amount: ", due)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Payment Successfully and Download the receipt")
                    print(f"BDT {due} has been sent to {Wnum}.")
                elif sub_choice == "5":
                    Inum = int(input("Enter Your Internet User account Number: "))
                    print("Your Internet User account Number: ", Inum)
                    due = int(input("Enter Your Due: "))
                    print("Your Due Amount: ", due)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Payment Successfully and Download the receipt")
                    print(f"BDT {due} has been sent to {Inum}.")
                elif sub_choice == "0":
                    break  # <-- This takes you back to main menu
                else:
                    print("Invalid choice, try again!")
        elif choice == "7":
            print("bKash")
            while True:
                print("bKash")
                print("1. Check Balance")
                print("2. Request Statement")
                print("3. Change Pin")
                print("4. Priyo Numbers")
                print("5. Save Bill")
                print("6. Helpline")
                print("0. Back to Main Menu")
                sub_choice = input("Enter your Choice: ")
                if sub_choice == "1":
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Current Balacnce TK:--")
                elif sub_choice == "2":
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Statement List:")
                elif sub_choice == "3":
                    num = int(input("old pin: "))
                    print("Your old pin: ", num)
                    newpin = int(input("Enter New Pin: "))
                    print("New PIN: ", newpin)
                    pin = input("Enter Menu Pin to Confirm: ")
                    print("Your Pin has been Changed Successfully!")
                elif sub_choice == "4":
                    print("bKash")
                    while True:
                        print("1. Send Money")
                        print("2. Cash Out")
                        print("0. Menu")
                        sub_choice = input("Enter your Choice: ")
                        if sub_choice == "1":
                            #how can i go back to main menu choose send send money option automatically?
                            print("still under construction")
                        elif sub_choice== "2":
                            print("still under construction")
                        elif sub_choice == "0":
                            break
                        else:
                            print("Invalid choice, try again!")
                elif sub_choice == "5":
                        print("bKash")
                        while True:
                            print("1. Add Bill Info")
                            print("2. Delete Bill Info")
                            print("3. View Saved Bill Info")
                            print("0. Menu")
                            sub_choice = input("Enter your Choice: ")
                            if sub_choice == "1":
                                send_money()
                            elif sub_choice== "2":
                                print("still under construction of View Saved Bill Info")
                            elif sub_choice== "3":
                                print("still under construction of View Saved Bill Info")
                            elif sub_choice== "0":
                                break
                            else:
                                print("Invalid choice, try again!")
                elif sub_choice == "6":
                    print("Call 16247 or Visit www.bKash.com for more info.")
                elif sub_choice == "0":
                    break  # <-- This takes you back to main menu
                else:
                    print("Invalid choice, try again!")
        elif choice == "0":
            break
list_operations()