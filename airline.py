import csv
import os

from booking_manager import BookingManager
from constants import CSV_FILE
from constants import FILE_HEADERS

def main():
    # Initialise booking manager class 
    booking_manager = BookingManager()

    # If csv file doesn't exist, we create a new file with the file headers
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as db_write:
            writer = csv.writer(db_write)
            writer.writerow(FILE_HEADERS)
    
    try:
        # Infinite loop to allow user to select options, can be exited via option 6 or keyboard interrupt (ctrl+c)
        while True:
            print("\nAirline Reservation System")
            print("------------------------")
            print("        MAIN MENU")
            print("------------------------")
            print("1.Book a ticket")
            print("2.Cancel a ticket")
            print("3.View available seats")
            print("4.Update your booking")
            print("5.View ticket information")
            print("6.Exit\n")

            # Prompts user to select an option provided
            option = input("Please select one of the options - ")

            # If statement that determines option and calls BookingManager class to perform the operation
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
            # If input is something we don't expect, we tell the user this and prompt them to try again 
            else:
                print("Option entered is invalid, please try again.")
    # If program is interrupted with ctrl+c, we exit gracefully
    except KeyboardInterrupt:
        print("\nExiting application, thank you for booking with us")


# Entrypoint into program
if __name__ == "__main__":
    main()
