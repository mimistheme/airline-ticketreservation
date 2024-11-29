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
        booking_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_reservation = Reservation(first_name, last_name, customer_id, ticket_number, seat, booking_time)

        print(f"\nCreated reservation for {new_reservation.first_name} {new_reservation.last_name} at {new_reservation.booking_time}")
        new_reservation.print_reservation_details()
        self.booking_helper.print_remaining_seat_amount(current_bookings, True)

        with open(CSV_FILE, mode='a', newline='') as db_write:
            writer = csv.writer(db_write)
            writer.writerow(new_reservation.to_csv_row())

        return
    
    
    def cancel_ticket(self):
        print("\nCancelling ticket")
        ticket_number = input("Please enter your ticket number - ")

        current_bookings = self.booking_helper.get_current_bookings()

        try:
            current_bookings.pop(ticket_number)
        except KeyError:
            print("\nThis booking could not be found.\n")
            return
            
        self.booking_helper.update_bookings_file(current_bookings)

        print(f"\nBooking with ticket number {ticket_number} has been cancelled successfully.\n")
        self.booking_helper.print_remaining_seat_amount(current_bookings)
        return


    def view_available_seats(self):
        # Get current bookings, transform seat numbers to set, loop through all numbers to 100 and check set
        print("Viewing available seats")
        return


    def update_booking(self):
        print("Updating booking")
        ticket_number = input("Please enter your ticket number - ")
        
        booking = self.booking_helper.get_booking(ticket_number)

        if booking is None:
            print("\nThis booking does not exist.\n")
            return
        
        booking.print_reservation_details()

        print("Please enter your updated details or leave empty to keep current details")

        updated_first_name = input("Please enter an updated first name - ")
        updated_last_name = input("Please enter an updated last name - ")

        if updated_first_name:
            booking.first_name = updated_first_name
        
        if updated_last_name:
            booking.last_name = updated_last_name

        if updated_first_name or updated_last_name:
            updated_bookings = self.booking_helper.get_current_bookings()
            updated_bookings[booking.ticket_num] = booking
            self.booking_helper.update_bookings_file(updated_bookings)
        
        print("\nUpdated booking details")
        booking.print_reservation_details()

        return


    def view_ticket_information(self):
        print("Viewing booking information\n") 
        ticket_number = input("Please enter your ticket number - ")
        
        booking = self.booking_helper.get_booking(ticket_number)
        
        if booking is None:
            print("\nThis booking does not exist.\n")
        else:
            booking.print_reservation_details()

        return