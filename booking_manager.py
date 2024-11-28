import csv
import datetime

from reservation import Reservation
from booking_helper import BookingHelper
from constants import TOTAL_SEATS
from constants import CSV_FILE
from constants import FILE_HEADERS

class BookingManager:

    def __init__(self):
        self.booking_helper = BookingHelper()


    def book_ticket(self):
        print("\nBooking ticket")
        first_name = input("Please enter your first name - ")
        last_name = input("Please enter your last name - ")

        current_bookings = self.booking_helper.get_current_bookings()
        if len(current_bookings) == TOTAL_SEATS:
            print("\nThere are no free seats left on this flight")
            return
        customer_id = self.booking_helper.generate_customer_id(current_bookings)
        ticket_number = self.booking_helper.generate_ticket_number(customer_id)
        seat = self.booking_helper.get_unassigned_seat(current_bookings)
        booking_time = datetime.datetime.now()
        new_reservation = Reservation(first_name, last_name, customer_id, ticket_number, seat, booking_time)
        new_reservation.print_reservation_details(current_bookings)

        with open(CSV_FILE, mode='a', newline='') as db_write:
            writer = csv.writer(db_write)
            writer.writerow([first_name, last_name, customer_id, ticket_number, seat, booking_time])

        return
    
    
    def cancel_ticket(self):
        print("\nCancelling ticket")
        ticket_number = input("Please enter your ticket number - ")

        updated_file_entries = []
        current_bookings = self.booking_helper.get_current_bookings()

        for reservation in current_bookings:
            if reservation.ticket_num != ticket_number:
                updated_file_entries.append(reservation.to_csv_row())

        if len(current_bookings) == len(updated_file_entries):
            print(f"\nA booking with the ticket number {ticket_number} does not exist")
            print("\n Returning to main menu...\n")
            return
            
        with open(CSV_FILE, mode='w', newline='') as db_write:
            writer = csv.writer(db_write)
            writer.writerow(FILE_HEADERS)
            
            for entry in updated_file_entries:
                writer.writerow(entry)

        print(f"\nBooking with ticket number {ticket_number} has been cancelled successfully.\n")
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