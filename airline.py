import csv
import random
import datetime

from reservation import Reservation

CSV_FILE = 'database.csv'
TOTAL_SEATS = 100

# Method to get current bookings by reading the database csv file
def get_current_bookings():
    current_bookings = []
    with open(CSV_FILE, mode='r') as db_read:
        reader = csv.reader(db_read)
        # Skip header line
        next(reader)
        for row in reader:
            current_bookings.append(Reservation(row[0], row[1], row[2], row[3], row[4], row[5]))

    return current_bookings


# Method to get an unassigned seat from the plane (this isn't the most efficient)
def get_unassigned_seat(current_bookings):
    # Convert list of reservations into a set of just the assigned seats
    assigned_seats = {int(booking.seat) for booking in current_bookings}
    assigned_seat = None
    # Randomly assign a seat number until we don't find a collision (this can probably be improved,
    # if we have 99 seat assignments we will be stuck in the loop until rand int finds the one remaining seat)
    while assigned_seat is None:
        temp_seat = random.randint(1,TOTAL_SEATS)
        if temp_seat not in assigned_seats:
            assigned_seat = temp_seat

    return assigned_seat


# Method to get an unassigned customer id
def generate_customer_id(current_bookings):
    # Convert list of reservations into a set of just the assigned customer_ids
    used_customer_ids = {int(booking.customer_id) for booking in current_bookings}
    customer_id = None
    # Randomly assign a customer id until we don't find a collision
    while customer_id is None:
        temp_customer_id = random.randint(100,999)
        if temp_customer_id not in used_customer_ids:
            customer_id = temp_customer_id

    return customer_id


def generate_ticket_number(customer_id):
    return str(customer_id) + '-' + str(random.randint(10000,99999))


def book_ticket():
    print("\nBooking ticket")
    first_name = input("Please enter your first name - ")
    last_name = input("Please enter your last name - ")

    current_bookings = get_current_bookings()
    if len(current_bookings) == TOTAL_SEATS:
        print("\nThere are no free seats left on this flight")
        return
    customer_id = generate_customer_id(current_bookings)
    ticket_number = generate_ticket_number(customer_id)
    seat = get_unassigned_seat(current_bookings)
    booking_time = datetime.datetime.now()
    new_reservation = Reservation(first_name, last_name, customer_id, ticket_number, seat, booking_time)
    new_reservation.print_reservation_details(current_bookings)

    with open(CSV_FILE, mode='a', newline='') as db_write:
        writer = csv.writer(db_write)
        writer.writerow([first_name, last_name, customer_id, ticket_number, seat, booking_time])

    return


def cancel_ticket():
    print("Cancelling ticket")
    return


def view_available_seats():
    print("Viewing available seats")
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
            view_available_seats()
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
