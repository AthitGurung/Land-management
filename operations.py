import os
from datetime import datetime, timedelta
from read import read_land_info
from write import write_land_info


def display_available_lands():
    """
    Display available lands.
    """
    land_info = read_land_info()
    for land_id, details in land_info.items():
        if details["availability"] == "Available":
            print(f"Land ID: {land_id}, City/District: {details['city']}, Land Facing Direction: {details['direction']}, Area: {details['area']} anna")


def generate_invoice(land_id, city, direction, area, customer_name, rent_date, duration, total_amount):
    """
    Generate an invoice for renting land.
    """
    invoice_dir = "invoices"
    os.makedirs(invoice_dir, exist_ok=True)
    invoice_file = os.path.join(invoice_dir, f"rent_invoice_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt")

    with open(invoice_file, "w") as file:
        file.write("===== Rent Invoice =====\n\n")
        file.write(f"Land ID: {land_id}\n")
        file.write(f"City/District: {city}\n")
        file.write(f"Land Facing Direction: {direction}\n")
        file.write(f"Area of Land: {area} anna\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Rent Date: {rent_date}\n")
        file.write(f"Duration of Rent: {duration} months\n")
        file.write(f"Total Amount: NPR {total_amount}\n")


def rent_land():
    """
    Rent land and generate invoice.
    """
    land_info = read_land_info()
    land_id = int(input("Enter the ID of the land you want to rent: "))
    if land_id not in land_info:
        print("Invalid land ID. Please try again.")
        return

    if land_info[land_id]["availability"] == "Not Available":
        print("Land is already rented. Please choose another land.")
        return

    customer_name = input("Enter your name: ")
    duration = int(input("Enter the duration of rent (in months): "))
    rent_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total_amount = land_info[land_id]["price"] * duration

    land_info[land_id]["availability"] = "Not Available"
    write_land_info(land_info)

    generate_invoice(land_id, land_info[land_id]["city"], land_info[land_id]["direction"],
                     land_info[land_id]["area"], customer_name, rent_date, duration, total_amount)

    print("Land rented successfully!")


def return_land():
    """
    Return rented land and generate invoice.
    """
    land_info = read_land_info()
    land_id = int(input("Enter the ID of the rented land you want to return: "))
    if land_id not in land_info:
        print("Invalid land ID. Please try again.")
        return

    if land_info[land_id]["availability"] == "Available":
        print("Land is not rented. Please check the land ID.")
        return

    customer_name = input("Enter your name: ")
    duration = int(input("Enter the duration of the rent: "))
    rent_date = datetime.now() - timedelta(days=30 * duration)
    total_amount = land_info[land_id]["price"] * duration

    land_info[land_id]["availability"] = "Available"
    write_land_info(land_info)

    generate_invoice(land_id, land_info[land_id]["city"], land_info[land_id]["direction"],
                     land_info[land_id]["area"], customer_name, rent_date.strftime('%Y-%m-%d %H:%M:%S'),
                     duration, total_amount)

    print("Land returned successfully!")
