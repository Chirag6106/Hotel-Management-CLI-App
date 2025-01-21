import csv
import main


def generate_bill(customer_name, room_charges, food_charges, service_charges, payment_mode):
    total_amount = room_charges + food_charges + service_charges
    invoice_id = f"INV{len(read_bills()) + 1:03}" 

    bill = {
        "invoice_id": invoice_id,
        "customer_name": customer_name,
        "room_charges": room_charges,
        "food_charges": food_charges,
        "service_charges": service_charges,
        "total_amount": total_amount,
        "payment_status": "Paid" if payment_mode else "Pending",
        "payment_mode": payment_mode or "Not Specified"
    }

    save_bill(bill)
    print(f"\nBill generated successfully!")
    print(f"Invoice ID: {invoice_id}")
    print(f"Total Amount: {total_amount}\n")


def save_bill(bill):
    with open("data/bills.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=bill.keys())
        if file.tell() == 0:  
            writer.writeheader()
        writer.writerow(bill)


def read_bills():
    try:
        with open("data/bills.csv", mode="r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def display_bills():
    bills = read_bills()
    if not bills:
        print("\nNo bills found!")
    else:
        print("\n--------------------------------------")
        print("               All Bills")
        print("--------------------------------------")
        # Header row
        print(
            f"{'Invoice ID':<12} {'Customer Name':<15} {'Room Charges':<15} {'Food Charges':<15} {'Service Charges':<15} {'Total Amount':<15} {'Payment Status':<15} {'Payment Mode':<12}"
        )
        print("-" * 120)
        # Data rows
        for bill in bills:
            print(
                f"{bill['invoice_id']:<12} {bill['customer_name']:<15} {bill['room_charges']:<15} {bill['food_charges']:<15} {bill['service_charges']:<15} {bill['total_amount']:<15} {bill['payment_status']:<15} {bill['payment_mode']:<12}"
            )
        print("\n\n")
