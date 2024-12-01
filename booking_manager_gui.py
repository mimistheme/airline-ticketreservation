import datetime
import tkinter as tk
from tkinter import messagebox

from booking_helper import BookingHelper
from constants import TOTAL_SEATS
from constants import BOX_SIZE

class BookingManagerGUI:
    def __init__(self):
        self.booking_helper = BookingHelper()

    def book_ticket(self):
        # Check to see if flight is fully booked, if so, return early
        current_bookings = self.booking_helper.get_current_bookings()
        if len(current_bookings) == TOTAL_SEATS:
            messagebox.showerror("No seats left", "There are no free seats left on this flight!")
            return
        
        # Create a pop-up window for input
        input_window = tk.Toplevel()
        input_window.title("Book Ticket")
        input_window.geometry(BOX_SIZE)

        tk.Label(input_window, text="Booking ticket, please enter passenger's name").pack(pady=5)
        
        # Labels and entry fields for first and last name
        tk.Label(input_window, text="First Name:").pack(pady=5)
        first_name = tk.Entry(input_window, width=30)
        first_name.pack(pady=5)
        
        tk.Label(input_window, text="Last Name:").pack(pady=5)
        last_name = tk.Entry(input_window, width=30)
        last_name.pack(pady=5)
        
        # Function to handle the submission of the form
        def submit_booking():
            first_name_ = first_name.get()
            last_name_ = last_name.get()
            
            if not first_name_ or not last_name_:
                messagebox.showerror("Input Error", "Please enter both first and last names.")
                return

            booking = self.booking_helper.book_ticket_helper(first_name_, last_name_, current_bookings)
            details = booking.get_reservation_details_string()
            confirmation_string = (
                f"Ticket booked for {first_name_} {last_name_}!\n"
                f"{details}"
                "--------------------------------\n"
                f"{self.booking_helper.get_remaining_seat_amount_string(self.booking_helper.get_current_bookings())}"
            )
            messagebox.showinfo("Booking Successful", confirmation_string)
            input_window.destroy()  # Close the input window

        # Submit button to confirm the booking
        submit_button = tk.Button(input_window, text="Submit", command=submit_booking)
        submit_button.pack(pady=10)

    def cancel_ticket(self):
        # Create a pop-up window for input
        input_window = tk.Toplevel()
        input_window.title("Cancel Ticket")
        input_window.geometry(BOX_SIZE)

        tk.Label(input_window, text="Cancelling ticket, please enter ticket number to cancel").pack(pady=5)
        
        # Labels and entry fields for first and last name
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)
        
        # Function to handle the submission of the form
        def submit_cancellation():
            ticket_number_ = ticket_number.get()
            
            if not ticket_number_:
                messagebox.showerror("Input Error", "Please enter a ticket number")
                return
            try:
                self.booking_helper.cancel_ticket_helper(ticket_number_)
            except KeyError:
                messagebox.showerror("Booking not found", "This booking could not be found.")
                return
            # Get current time so we can print when the cancellation was processed to the user
            cancellation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            messagebox.showinfo("Canellation Successful", f"Booking with ticket number {ticket_number_} has been cancelled successfully at {cancellation_time}.")
            input_window.destroy()  # Close the input window

        # Submit button to confirm the booking
        submit_button = tk.Button(input_window, text="Submit", command=submit_cancellation)
        submit_button.pack(pady=10)


    def view_available_seats(self):
        messagebox.showinfo("View Seats", "Viewing available seats... (Functionality not implemented)")


    def update_booking(self):
        input_window = tk.Toplevel()
        input_window.title("Update Booking")
        input_window.geometry(BOX_SIZE)

        tk.Label(input_window, text="Updating booking information, please enter ticket number").pack(pady=5)
        
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)

         # Function to handle the submission of the form
        def submit_update_booking():
            ticket_number_ = ticket_number.get()
            
            if not ticket_number_:
                messagebox.showerror("Input Error", "Please enter a ticket number")
                return
            
            booking = self.booking_helper.get_booking(ticket_number_)

            # If None is returned from helper method, we return early as booking doesn't exist
            if booking is None:
                messagebox.showerror("Booking unavailable", "This booking does not exist.")
                return
            
            second_window = tk.Toplevel()
            second_window.title("Update Booking")
            second_window.geometry(BOX_SIZE)

            tk.Label(second_window, text="Updating booking information, please enter ticket number").pack(pady=5)
            
            # Labels and entry fields for first and last name
            tk.Label(second_window, text="First Name").pack(pady=5)
            first_name = tk.Entry(second_window, width=30)
            first_name.pack(pady=5)
        
            tk.Label(second_window, text="Last Name:").pack(pady=5)
            last_name = tk.Entry(second_window, width=30)
            last_name.pack(pady=5)

            def submit_updated_information():
                first_name_ = first_name.get()
                last_name_ = last_name.get()
                
                if not first_name_ or not last_name_:
                    messagebox.showerror("Input Error", "Please enter both first and last names.")
                    return
                
                updated_booking = self.booking_helper.update_ticket_helper(booking, first_name_, last_name_)
                
                messagebox.showinfo(f"{booking.ticket_num}", booking.get_reservation_details_string())
                second_window.destroy()

            submit_button_ = tk.Button(second_window, text="Submit", command=submit_updated_information)
            submit_button_.pack(pady=10)

            input_window.destroy()  # Close the input window

        # Submit button to confirm the booking
        submit_button = tk.Button(input_window, text="Submit", command=submit_update_booking)
        submit_button.pack(pady=10)
        

    def view_ticket_information(self):
        input_window = tk.Toplevel()
        input_window.title("View Ticket")
        input_window.geometry(BOX_SIZE)

        tk.Label(input_window, text="Viewing ticket information, please enter ticket number").pack(pady=5)
        
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)

        # Function to handle the submission of the form
        def submit_view_information():
            ticket_number_ = ticket_number.get()
            
            if not ticket_number_:
                messagebox.showerror("Input Error", "Please enter a ticket number")
                return
            
            booking = self.booking_helper.get_booking(ticket_number_)

            # If None is returned from helper method, we return early as booking doesn't exist
            if booking is None:
                messagebox.showerror("Booking unavailable", "This booking does not exist.")
            else:
                # Print details if reservation is returned
                messagebox.showinfo(f"{booking.ticket_num}", booking.get_reservation_details_string())

            input_window.destroy()  # Close the input window

        # Submit button to confirm the booking
        submit_button = tk.Button(input_window, text="Submit", command=submit_view_information)
        submit_button.pack(pady=10)
        