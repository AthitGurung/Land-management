LAND_FILE = "land.txt"


def write_land_info(land_stock):
    """
    Write the updated land stock to the file.
    """
    with open(LAND_FILE, "w") as file:
        for land_id, details in land_stock.items():
            line = f"{land_id}, {details['city']}, {details['direction']}, {details['area']}, {details['price']}, {details['availability']}\n"
            file.write(line)
