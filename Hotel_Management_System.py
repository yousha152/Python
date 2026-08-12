bookings = []

while True:
    print("===== HOTEL MANAGEMENT SYSTEM =====\n")

    print("1. Book Room")
    print("2. View Bookings")
    print("3. Check Out")
    print("4. Exit\n")

    print("Press the corresponding number to select an option.\n")

    choice = input("Enter your choice: ")

    # For booking a room
    if choice == '1':
        print("\n--- Book Room ---")

        # Customer Name
        while True:
            name = input("Enter customer name: ")

            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name. Try again.")

        # Room Number
        while True:
            room = input("Enter your room number: ")

            if room.isdigit():
                room = int(room)
                break
            else:
                print("Invalid room number. Try again.")

        # Number of Days
        while True:
            no_of_days = input("Enter number of days: ")

            if no_of_days.isdigit():
                no_of_days = int(no_of_days)
                break
            else:
                print("Invalid number of days. Try again.")

        bookings.append([name, room, no_of_days])

        print("Room booked successfully.\n")

    # For viewing bookings
    elif choice == '2':
        print("\n--- View Bookings ---")

        if not bookings:
            print("No bookings found.\n")
        else:
            print(f"{'Customer Name':<20}{'Room No':<10}{'Days'}")
            print("-" * 40)
                  

            for booking in bookings:
                print(f"{booking[0]:<20}{booking[1]:<10}{booking[2]}")

            print()

    # For checking out
    elif choice == '3':
        print("\n--- Check Out ---")

        while True:
            room = input("Enter your room number to check out: ")

            if room.isdigit():
                room = int(room)
                break
            else:
                print("Invalid room number. Try again.")

        for booking in bookings:
            if booking[1] == room:
                bookings.remove(booking)
                print("Checked out successfully.\n")
                break
        else:
            print("Room number not found. Please check your booking details.\n")

    # For exiting the program
    elif choice == '4':
        print("Exiting the program. Thank you for using the Hotel Management System.")
        break

    else:
        print("Invalid choice. Please try again.\n")