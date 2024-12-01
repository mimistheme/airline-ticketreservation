import datetime
import tkinter as tk
from tkinter import messagebox

from booking_helper import BookingHelper
from constants import TOTAL_SEATS

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
        input_window.geometry("300x200")

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

            self.booking_helper.book_ticket_helper(first_name_, last_name_, current_bookings)
            messagebox.showinfo("Booking Successful", f"Ticket booked for {first_name_} {last_name_}!")
            input_window.destroy()  # Close the input window

        # Submit button to confirm the booking
        submit_button = tk.Button(input_window, text="Submit", command=submit_booking)
        submit_button.pack(pady=10)

    def cancel_ticket(self):
        # Create a pop-up window for input
        input_window = tk.Toplevel()
        input_window.title("Cancel Ticket")
        input_window.geometry("300x200")

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
        messagebox.showinfo("Update Booking", "Updating booking... (Functionality not implemented)")

    def view_ticket_information(self):
        messagebox.showinfo("Ticket Info", "Viewing ticket information... (Functionality not implemented)")