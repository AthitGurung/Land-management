from operations import rent_land, return_land, display_available_lands


def main():
    while True:
        print("\n===== Welcome to Techno Property Nepal Pvt. Ltd =====")
        display_available_lands()

        choice = input("\nEnter '1' to rent land, '2' to return rented land, or '3' to quit: ").upper()

        if choice == '1':
            rent_land()

        elif choice == '2':
            return_land()

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")


if __name__ == "__main__":
    main()
