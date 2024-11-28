from booking_manager import BookingManager

def main():
    print("Airline Reservation System\n")

    booking_manager = BookingManager()

    while True:
        print("1.Book a ticket")
        print("2.Cancel a ticket")
        print("3.View available seats")
        print("4.Update your booking")
        print("5.View ticket information")
        print("6.Exit\n")

        option = input("Please select one of the options - ")

        if option == '1':
            booking_manager.book_ticket()
        elif option == '2':
            booking_manager.cancel_ticket()
        elif option == '3':
            booking_manager.view_available_seats()
        elif option == '4':
            booking_manager.update_booking()
        elif option == '5':
            booking_manager.view_ticket_information()
        elif option == '6':
            print("Exiting application, thank you for booking with us")
            break
        else:
            print("Option entered is invalid, please try again.")


if __name__ == "__main__":
    main()
