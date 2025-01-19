import csv

def check_room_availability(room_type):
    available_rooms = []
    with open('data/rooms.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['type'] == room_type and row['status'] == 'Available':
                available_rooms.append(row['room_no'])
    return available_rooms


def update_room_status(room_no, new_status):
    rows = []
    with open('data/rooms.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['room_no'] == room_no:
                row['status'] = new_status
            rows.append(row)
    
    with open('data/rooms.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)