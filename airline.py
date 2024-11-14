import csv
import random

from reservation import Reservation

CSV_FILE = 'database.csv'

def get_current_bookings():
    current_bookings = []
    with open(CSV_FILE, mode='r') as db_read:
        reader = csv.reader(db_read)
        next(reader)
        for row in reader:
            current_bookings.append(Reservation(row[0], row[1], row[2], row[3]))

    return current_bookings


def generate_customer_id(current_bookings):
    used_customer_ids = {booking.customer_id for booking in current_bookings}
    customer_id = None
    while customer_id is None:
        temp_customer_id = random.randint(100,999)
        if temp_customer_id not in used_customer_ids:
            customer_id = temp_customer_id

    return customer_id

def book_ticket():
    print("Booking ticket")
    current_bookings = get_current_bookings()
    customer_id = generate_customer_id(current_bookings)
    print("Generated customer id " + str(customer_id))

    # with open(CSV_FILE, mode='a', newline='') as db_write:

    return


def cancel_ticket():
    print("Cancelling ticket")
    return


def view_tickets():
    print("Viewing tickets")
    return


def update_booking():
    print("Updating booking")
    return


def view_ticket_information():
    print("Viewing ticket information")
    return


def main():
    print("Airline Reservation System\n")

    while True:
        print("1.Book a ticket")
        print("2.Cancel a ticket")
        print("3.View available seats")
        print("4.Update your booking")
        print("5.View ticket information")
        print("6.Exit\n")

        option = input("Please select one of the options - ")

        if option == '1':
            book_ticket()
        elif option == '2':
            cancel_ticket()
        elif option == '3':
            view_tickets()
        elif option == '4':
            update_booking()
        elif option == '5':
            view_ticket_information()
        elif option == '6':
            print("Exiting application, thank you for booking with us")
            break
        else:
            print("Option entered is invalid, please try again.")


if __name__ == "__main__":
    main()
