import csv
import datetime

from reservation import Reservation
from booking_helper import BookingHelper
from constants import TOTAL_SEATS
from constants import CSV_FILE

class BookingManager:

    def __init__(self):
        self.booking_helper = BookingHelper()

    # Method to book ticket by gathering necessary information from customer and saving it to csv database
    def book_ticket(self):
        print("\nBooking ticket")
        # Prompting user for name input
        first_name = input("Please enter your first name - ")
        last_name = input("Please enter your last name - ")

        # Check to see if flight is fully booked, if so, return early
        current_bookings = self.booking_helper.get_current_bookings()
        if len(current_bookings) == TOTAL_SEATS:
            print("\nThere are no free seats left on this flight")
            return

        new_reservation = self.booking_helper.book_ticket_helper(first_name, last_name, current_bookings)

        # Print information about booking as well as remaining seat information
        print(f"\nCreated reservation for {new_reservation.first_name} {new_reservation.last_name} at {new_reservation.booking_time}")
        new_reservation.print_reservation_details()
        # We call the booking helper to get an updated version of the current bookings object so our remaining seat count is accurate
        self.booking_helper.print_remaining_seat_amount(self.booking_helper.get_current_bookings())
    
    
    # Method to cancel ticket by asking user for ticket number, checking if booking exists and removing it if it does
    def cancel_ticket(self):
        print("\nCancelling ticket")
        # Prompting user to input ticket number to cancel
        ticket_number = input("Please enter your ticket number - ")

        try:
            current_bookings = self.booking_helper.cancel_ticket_helper(ticket_number)
        except KeyError:
            return

        # Get current time so we can print when the cancellation was processed to the user
        cancellation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Print information about booking cancellation as well as remaining seat information
        print(f"\nBooking with ticket number {ticket_number} has been cancelled successfully at {cancellation_time}.\n")
        self.booking_helper.print_remaining_seat_amount(current_bookings)

    
    # Method to view seat layout (see available, occupied and window seats) as well as printing ticket information of occupied window seats
    def view_available_seats(self):
        print("Viewing available seats")

        current_bookings = self.booking_helper.get_current_bookings()
        occupied_seats = set()

        # Look through current bookings and add the ticket number to a set
        for booking in current_bookings.values():
            occupied_seats.add(int(booking.seat))
            # If occupied seat is a window seat, we print information about this booking
            if (self.booking_helper.is_window_seat(booking.seat)):
                print(f"Window seat {booking.seat} is occupied by {booking.first_name} {booking.last_name} with ticket number {booking.ticket_num}")

        print("\n----------------------------")
        print("        PLANE LAYOUT")
        print("----------------------------")
        
        plane_layout = []
        # Loop through total number of seats on plane to create a top down view of plane's current booking status
        for i in range(1, TOTAL_SEATS+1):
            # Default presentation of an unoccupied seat is just the seat number
            seat = str(i)
            # If seat number is in occupied seats set, change the presentation to an X to signify occupied
            if i in occupied_seats:
                seat = "X"
            # If seat number is determined to be window seat, prefix with new line (as window seats start a row) and add a (W) to denote window seat
            if self.booking_helper.is_window_seat(i):
                seat = "\n" + seat + "(W)"
            
            # Add | to improve visualisation of individual seats
            seat = seat + " | "
            # Append the modified seat number to list of all seats
            plane_layout.append(seat)
        
        # Join list of formatted seats into a single string to print, as we prefixed each window seat with \n, we should get a plane layout with rows of 3 seats
        print("".join(plane_layout))

        # Print key to allow user to understand the output
        print("\nKey:")
        print("(W) - Window seat")
        print("X - Occupied seat")


    # Method to update an existing booking, takes an input of ticket number and allows user to change name on the booking
    def update_booking(self):
        print("Updating booking")
        # Prompting user to input ticket number to update
        ticket_number = input("Please enter your ticket number - ")
        
        # Getting booking by calling helper method
        booking = self.booking_helper.get_booking(ticket_number)

        # If None is returned from helper method, we return early as booking doesn't exist
        if booking is None:
            print("\nThis booking does not exist.\n")
            return
        
        booking.print_reservation_details()

        # Prompting user to input updated information about booking, if user inputs nothing we leave the first/last name as is
        print("Please enter your updated details or leave empty to keep current details")
        updated_first_name = input("Please enter an updated first name - ")
        updated_last_name = input("Please enter an updated last name - ")

        updated_booking = self.booking_helper.update_ticket_helper(booking, updated_first_name, updated_last_name)
        
        print("\nUpdated booking details")
        updated_booking.print_reservation_details()

    # Method to print booking information of an existing booking
    def view_ticket_information(self):
        print("Viewing booking information\n") 
        # Prompting user to input ticket number to display information of
        ticket_number = input("Please enter your ticket number - ")
        
        booking = self.booking_helper.get_booking(ticket_number)
        
        # If None is returned from helper method, we return early as booking doesn't exist
        if booking is None:
            print("\nThis booking does not exist.\n")
        else:
            # Print details if reservation is returned
            booking.print_reservation_details()