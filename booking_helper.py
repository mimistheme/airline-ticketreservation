import csv
import random

from constants import TOTAL_SEATS
from constants import CSV_FILE
from reservation import Reservation


class BookingHelper:

     # Method to get current bookings by reading the database csv file
    def get_current_bookings(self):
        current_bookings = []
        with open(CSV_FILE, mode='r') as db_read:
            reader = csv.reader(db_read)
            # Skip header line
            next(reader)
            for row in reader:
                current_bookings.append(Reservation(row[0], row[1], row[2], row[3], row[4], row[5]))

        return current_bookings


    # Method to get an unassigned seat from the plane (this isn't the most efficient)
    def get_unassigned_seat(self, current_bookings):
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
    def generate_customer_id(self, current_bookings):
        # Convert list of reservations into a set of just the assigned customer_ids
        used_customer_ids = {int(booking.customer_id) for booking in current_bookings}
        customer_id = None
        # Randomly assign a customer id until we don't find a collision
        while customer_id is None:
            temp_customer_id = random.randint(100,999)
            if temp_customer_id not in used_customer_ids:
                customer_id = temp_customer_id

        return customer_id


    def generate_ticket_number(self, customer_id):
        return str(customer_id) + '-' + str(random.randint(10000,99999))

