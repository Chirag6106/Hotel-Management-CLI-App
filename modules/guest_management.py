import csv
import main
from modules import room_management as rooms

def check_in_guest():
        print("--------------------------------------")
        print("           Guest Check-In             ")
        print("--------------------------------------")
        room_type = input("Enter Room Type (Single/Double): ")
        available_rooms = rooms.check_room_availability(room_type)
        if not available_rooms:
            main.clear()
            print(f"No {room_type} rooms are available at the moment. Please try a different room type.")
            return
        print(f"Available {room_type} rooms: {', '.join(available_rooms)}")
        room_no = input("Enter the room number to assign (from the above list): ")
        if room_no not in available_rooms:
            main.clear()
            print("Invalid room number selected. Please restart the check-in process.")
            return

        name = input("Enter Guest Name: ")
        guest_id = input("Enter ID Number: ")
        contact = input("Enter Contact Number: ")
        check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")

        rooms.update_room_status(room_no, "Occupied")

        with open('data/guests.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, guest_id, contact, room_type, check_in_date])
        main.clear()
        print(f"Guest {name} checked in successfully!")


def view_guest_information():
    print("--------------------------------------")
    print("          View Guest Information       ")
    print("--------------------------------------")
    with open('data/guests.csv', 'r') as file:
        reader = csv.reader(file)
        print(f"{'Name':<15} {'ID':<12} {'Contact':<15} {'Room Type':<10} {'Check-In Date':<12}")
        print("-" * 65)
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<12} {row[2]:<15} {row[3]:<10} {row[4]:<12}")