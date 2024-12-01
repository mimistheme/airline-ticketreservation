import csv
import random

from datetime import datetime
from constants import TOTAL_SEATS
from constants import CSV_FILE
from constants import FILE_HEADERS
from reservation import Reservation

# Class used to help with booking operations, this class is re-used for both the Text and GUI booking managers
class BookingHelper:

    # Helper method to book ticket, re-used between text and GUI, returns Reservation object of the new reservation
    def book_ticket_helper(self, first_name, last_name, current_bookings):
        # Generate booking information by using helper functions
        customer_id = self.generate_customer_id(current_bookings)
        ticket_number = self.generate_ticket_number(customer_id)
        seat = self.get_unassigned_seat(current_bookings)
        # Check current time and transform to YYYY/MM/DD HH/MM/SS format to store booking time
        booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Create Reservation object from above values
        new_reservation = Reservation(first_name, last_name, customer_id, ticket_number, seat, booking_time)

        # Write the new booking to the end of csv file
        with open(CSV_FILE, mode='a', newline='') as db_write:
            writer = csv.writer(db_write)
            writer.writerow(new_reservation.to_csv_row())
        
        return new_reservation
    
    # Helper method to cancel ticket, re-used between text and GUI, returns updated dictionary of current bookings
    def cancel_ticket_helper(self, ticket_number):
        # Get current bookings, object returned is a dictionary with the key being ticket number
        current_bookings = self.get_current_bookings()

        # Try to access dictionary, if value doesn't exist we get a KeyError and can return early as this booking doesn't exist
        try:
            current_bookings.pop(ticket_number)
        except KeyError:
            print("\nThis booking could not be found.")
            raise KeyError

        # Call helper method to overwrite bookings file without the booking we want cancelled
        self.update_bookings_file(current_bookings)

        return current_bookings


    # Method to get current bookings as a dictionary by reading the database csv file
    def get_current_bookings(self):
        current_bookings = {}
        with open(CSV_FILE, mode='r') as db_read:
            reader = csv.reader(db_read)
            # Skip header line
            next(reader)
            # Loop through each row in csv and create Reservation class for each entry
            # Set the ticket number as the key for each reservation
            for row in reader:
                reservation = Reservation(row[0], row[1], row[2], row[3], row[4], row[5])
                current_bookings[reservation.ticket_num] = reservation

        return current_bookings
    
    
    # Method to query a specific booking and return it from dictionary
    def get_booking(self, ticket_number):
        current_bookings = self.get_current_bookings()
        return current_bookings.get(ticket_number)
    

    # Method used to overwrite the whole existing file in case we make any modifications to existing bookings
    def update_bookings_file(self, current_bookings):
        with open(CSV_FILE, mode='w', newline='') as db_write:
            writer = csv.writer(db_write)
            # We write the file headers to the first row to make sure they are maintained and not overwritten by bookings
            writer.writerow(FILE_HEADERS)
            
            # Loop through each booking and write to csv file
            for entry in current_bookings.values():
                writer.writerow(entry.to_csv_row())


    # Method to get an unassigned seat from the plane (this isn't the most efficient)
    def get_unassigned_seat(self, current_bookings):
        # Convert list of reservations into a set of just the assigned seats
        assigned_seats = {int(booking.seat) for booking in current_bookings.values()}
        assigned_seat = None
        # Randomly assign a seat number until we don't find a collision (this can probably be improved,
        # if we have 99 seat assignments we will be stuck in the loop until rand int finds the one remaining seat)
        while assigned_seat is None:
            temp_seat = random.randint(1,TOTAL_SEATS)
            if temp_seat not in assigned_seats:
                assigned_seat = temp_seat

        return assigned_seat


    # Method to calculate remaining seat count and print the value
    def print_remaining_seat_amount(self, current_bookings):
        remaining_seats = 100 - len(current_bookings)
        print(f"There are {remaining_seats} seats remaining\n")

    
    # Method to get an unassigned customer id
    def generate_customer_id(self, current_bookings):
        # Convert list of reservations into a set of just the assigned customer_ids
        used_customer_ids = {int(booking.customer_id) for booking in current_bookings.values()}
        customer_id = None
        # Randomly assign a customer id until we don't find a collision
        while customer_id is None:
            temp_customer_id = random.randint(100,999)
            if temp_customer_id not in used_customer_ids:
                customer_id = temp_customer_id

        return customer_id


    # Method to generate ticket number by concatenating customerId, '-' and a random 5 digit integer
    def generate_ticket_number(self, customer_id):
        return str(customer_id) + '-' + str(random.randint(10000,99999))
    
    
    # Method to determine whether a seat is a window seat. Window seats are every 3rd seat starting from 1 (so 1,4,7,10...)
    # We use % (modulo) to determine the divison remainder, if the output is 0 it means the number is divisible 
    # As our sequence starts from 1, we need to add 2 to the seat number to determine if it is divisible by 3 and part of our sequence
    def is_window_seat(self, seat_number):
        return (int(seat_number) + 2) % 3 == 0
