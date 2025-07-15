LAND_FILE = "land_info.txt"


def read_land_info():
    """
    Read the land info file and return a dictionary of land details.
    """
    land_info = {}
    with open(LAND_FILE, "r") as file:
        for line in file:
            land_details = line.strip().split(", ")
            land_id = int(land_details[0])
            availability = land_details[-1]
            land_info[land_id] = {
                "city": land_details[1],
                "direction": land_details[2],
                "area": int(land_details[3]),
                "price": int(land_details[4]),
                "availability": availability
            }
    return land_info
