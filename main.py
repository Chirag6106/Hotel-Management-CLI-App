import os
from modules import auth
from modules import billing
from modules import guest_management
from modules import housekeeping
from modules import reports
from modules import reservation_management
from modules import room_management


def displayMainMenu():
    print("--------------------------------------")
    print("\tHotel Management System")
    print("--------------------------------------")
    print("1. Guest Management")
    print("2. Room Management")
    print("3. Reservation Management")
    print("4. Billing and Payments")
    print("5. Reports and Analytics")
    print("6. Maintenance and Housekeeping")
    print("7. Exit")
    print("--------------------------------------")
    choise = int(input("Please choose an option (1-7):"))
    return choise

def run_guest_management():
    while True:
        print("--------------------------------------")
        print("          Guest Management            ")
        print("--------------------------------------")
        print("1. Check-In Guest")
        print("2. View Guest Information")
        print("3. Back to Main Menu")
        print("--------------------------------------")
        choice = input("Please choose an option (1-3): ")
        
        if choice == "1":
            clear()
            guest_management.check_in_guest()
        elif choice == "2":
            clear()
            guest_management.view_guest_information()
        elif choice == "3":
            clear()
            break
        else:
            print("Invalid choice. Please try again.")


def run_room_management():
    pass
def run_reservation_management():
    pass
def run_billing_and_payments():
    clear()
    while True:
        print("--------------------------------------")
        print("            Billing Menu              ")
        print("--------------------------------------")
        print("1. Generate Bill")
        print("2. View All Bills")
        print("3. Back to Main Menu")
        print("--------------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            customer_name = input("Enter customer name: ")
            try:
                room_charges = float(input("Enter room charges: "))
                food_charges = float(input("Enter food charges: "))
                service_charges = float(input("Enter service charges: "))
            except ValueError:
                print("Invalid input! Charges must be numbers.")
                continue

            payment_mode = input("Enter payment mode (Cash/Card/UPI): ")

            clear()
            billing.generate_bill(customer_name, room_charges, food_charges, service_charges, payment_mode)

        elif choice == "2":
            clear()
            billing.display_bills()

        elif choice == "3":
            clear()
            break
        else:
            print("Invalid choice. Please try again.")

def run_reports_and_analytics():
    pass
def run_maintenance_and_housekeeping():
    pass
       
#       CLEAR TERMINAL
def clear():
    if os.name == 'nt':
        os.system('cls')


#       MAIN FUNCTION
def main():
    clear()
    print("Welcome to the system please log in")
    while True:
        authresult = auth.authuser()
        if authresult == True:
            clear()
            print("Login successfully")
            break
        else:
            print("Incorrect username and password! please try again")
        
    while True:
        choice = displayMainMenu()
        
        if choice == 1:
            clear()
            run_guest_management()
        elif choice == 2:
            run_room_management()
        elif choice == 3:
            run_reservation_management()
        elif choice == 4:
            run_billing_and_payments()
        elif choice == 5:
            run_reports_and_analytics()
        elif choice == 6:
            run_maintenance_and_housekeeping()
        elif choice == 7:
            print("Exiting the system. Goodbye!")
            break
        else:
            clear()
            print("Invalid choice. Please try again.")



if __name__ == "__main__" :
    main()