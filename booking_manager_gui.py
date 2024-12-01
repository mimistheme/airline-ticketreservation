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
        # Check to see if flight is fully booked, if so, return dispaly error and return early
        current_bookings = self.booking_helper.get_current_bookings()
        if len(current_bookings) == TOTAL_SEATS:
            messagebox.showerror("No seats left", "There are no free seats left on this flight!")
            return
        
        # Create a pop-up window for the input
        input_window = tk.Toplevel()
        input_window.title("Book Ticket")
        tk.Label(input_window, text="Booking ticket, please enter passenger's name").pack(pady=5)
        
        # Create labels and entry fields for first and last name input
        tk.Label(input_window, text="First Name:").pack(pady=5)
        first_name = tk.Entry(input_window, width=30)
        first_name.pack(pady=5)
        
        tk.Label(input_window, text="Last Name:").pack(pady=5)
        last_name = tk.Entry(input_window, width=30)
        last_name.pack(pady=5)
        
        # Method to handle submission of passenger detail form
        def submit_booking():
            first_name_ = first_name.get()
            last_name_ = last_name.get()
            
            # If first or last name are empty, display error box and return early
            if not first_name_ or not last_name_:
                messagebox.showerror("Input Error", "Please enter both first and last names.")
                return

            # Book ticket for customer and display ticket and remaining seat information in pop-up box
            booking = self.booking_helper.book_ticket_helper(first_name_, last_name_, current_bookings)
            details = booking.get_reservation_details_string()
            confirmation_string = (
                f"Ticket booked for {first_name_} {last_name_}!\n"
                f"{details}"
                "--------------------------------\n"
                f"{self.booking_helper.get_remaining_seat_amount_string(self.booking_helper.get_current_bookings())}"
            )
            messagebox.showinfo("Booking Successful", confirmation_string)

            # Close the input window
            input_window.destroy() 

        # Render submit button to confirm the booking and invoke the submit_booking method
        submit_button = tk.Button(input_window, text="Submit", command=submit_booking)
        submit_button.pack(pady=10)

    def cancel_ticket(self):
        # Create a pop-up window for the input
        input_window = tk.Toplevel()
        input_window.title("Cancel Ticket")
        tk.Label(input_window, text="Cancelling ticket, please enter ticket number to cancel").pack(pady=5)
        
        # Create labels and entry fields for ticket number input
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)
        
        # Method to handle submission of ticket number for cancellation
        def submit_cancellation():
            ticket_number_ = ticket_number.get()
            
            # If ticket number is an empty string, show error box and return early
            if not ticket_number_:
                messagebox.showerror("Input Error", "Please enter a ticket number")
                return
            
            # Try to cancel ticket, if a KeyError is thrown (no booking found with that ticket number) show error box and return early
            try:
                current_bookings = self.booking_helper.cancel_ticket_helper(ticket_number_)
            except KeyError:
                messagebox.showerror("Booking not found", "This booking could not be found.")
                return
            
            # Get current time so we can display when the cancellation was processed to the user
            cancellation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Format cancellation confirmation string
            confirmation_string = (
                f"Booking with ticket number {ticket_number_} has been cancelled successfully at {cancellation_time}.\n"
                "--------------------------------\n"
                f"{self.booking_helper.get_remaining_seat_amount_string(current_bookings)}"
            )
            messagebox.showinfo("Canellation Successful", confirmation_string)
        
            # Close the input window
            input_window.destroy() 

        # Render submit button to confirm the booking and invoke the submit_cancellation method
        submit_button = tk.Button(input_window, text="Submit", command=submit_cancellation)
        submit_button.pack(pady=10)


    def view_available_seats(self):
        # Create a new window for the display
        layout_window = tk.Toplevel()
        layout_window.title("Available Seats")
        layout_window.geometry("500x1000")

        occupied_seats = self.booking_helper.view_available_seats_helper()

        # Create header for the plane layout
        tk.Label(layout_window, text="----------------------------", font=("Helvetica", 12)).pack()
        tk.Label(layout_window, text="PLANE LAYOUT", font=("Helvetica", 14, "bold")).pack()
        tk.Label(layout_window, text="----------------------------", font=("Helvetica", 12)).pack()

        # Create a frame to allow us to create a grid layout of boxes
        layout_frame = tk.Frame(layout_window)
        layout_frame.pack(pady=10)

        seats_per_row = 3

        for i in range(1, TOTAL_SEATS + 1):
            # Default presentation of an unoccupied seat is the seat number and a green box
            text = f"{i}"  # Empty seat
            bg = "green"

            # If seat number is in the occupied seats set, change the presentation to an X and a red box to signify occupied
            if i in occupied_seats:
                text = "X"  # Occupied
                bg = "red"
            # If seat number is determined to be window seat, change the seat to have a (W) and be blue (occupied seats are unaffected by this)
            elif self.booking_helper.is_window_seat(i):
                text = f"{i}(W)"  # Window seat
                bg = "lightblue"

            # Format the  label to look like a box for the seat based on its status
            # bg gives it a colourful background, relief gives the label a border
            label = tk.Label(layout_frame, text=text, bg=bg, width=6, height=1, relief="ridge", font=("Helvetica", 10))

            # Calculate the position of the seat in the grid
            # Row calculated by floor division of index by number of seats in row
            # Column calculated by modulo of index by number of seats in row
            # [0,0] [0,1] [0,2]
            # [1,0] [1,1] [1,2]
            # [2,0] [2,1] [2,2]...
            row = (i - 1) // seats_per_row
            column = (i - 1) % seats_per_row
            label.grid(row=row, column=column, padx=1, pady=1)

        # Formats and populates the key section at the bottom of the display
        tk.Label(layout_window, text="Key:", font=("Helvetica", 12, "bold")).pack(anchor="w", padx=10)
        tk.Label(layout_window, text="(W) - Window seat", font=("Helvetica", 12)).pack(anchor="w", padx=10)
        tk.Label(layout_window, text="X - Occupied seat", font=("Helvetica", 12)).pack(anchor="w", padx=10)


    def update_booking(self):
        # Create a pop-up window for the input
        input_window = tk.Toplevel()
        input_window.title("Update Booking")
        tk.Label(input_window, text="Updating booking information, please enter ticket number").pack(pady=5)
        
        # Create labels and entry fields for ticket number input
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)

        # Method to handle submission of ticket number for update
        def submit_update_booking():
            ticket_number_ = ticket_number.get()
            
            # If ticket number is an empty string, show error box and return early
            if not ticket_number_:
                messagebox.showerror("Input Error", "Please enter a ticket number")
                return
            
            booking = self.booking_helper.get_booking(ticket_number_)

            # If None is returned from helper method, we return early as booking doesn't exist
            if booking is None:
                messagebox.showerror("Booking unavailable", "This booking does not exist.")
                return
            
            # Render a second window to allow user to enter updated information
            second_window = tk.Toplevel()
            second_window.title("Update Booking")
            tk.Label(second_window, text="Updating booking information, please enter updated information.").pack(pady=5)
            tk.Label(second_window, text="Fields left empty will be kept the same.").pack(pady=3)

            
            # Create labels and entry fields for first and last name input
            tk.Label(second_window, text="First Name").pack(pady=5)
            first_name = tk.Entry(second_window, width=30)
            first_name.pack(pady=5)
        
            tk.Label(second_window, text="Last Name:").pack(pady=5)
            last_name = tk.Entry(second_window, width=30)
            last_name.pack(pady=5)

            # Method to handle submission of updated ticket information
            def submit_updated_information():
                first_name_ = first_name.get()
                last_name_ = last_name.get()
            
                updated_booking = self.booking_helper.update_ticket_helper(booking, first_name_, last_name_)
                
                # Display updated reservation details
                messagebox.showinfo(f"{updated_booking.ticket_num}", updated_booking.get_reservation_details_string())
                second_window.destroy()

            # Render submit button for second window to confirm the updated information and invoke the submit_updated_information method
            submit_button_ = tk.Button(second_window, text="Submit", command=submit_updated_information)
            submit_button_.pack(pady=10)

            # Close the input window
            input_window.destroy() 

        # Render submit button to submit ticket number and invoke the submit_update_booking method
        submit_button = tk.Button(input_window, text="Submit", command=submit_update_booking)
        submit_button.pack(pady=10)
        

    def view_ticket_information(self):
        # Create a pop-up window for the input
        input_window = tk.Toplevel()
        input_window.title("View Ticket")
        tk.Label(input_window, text="Viewing ticket information, please enter ticket number").pack(pady=5)
        
        # Create labels and entry fields for ticket number input
        tk.Label(input_window, text="Ticket Number:").pack(pady=5)
        ticket_number = tk.Entry(input_window, width=30)
        ticket_number.pack(pady=5)

        # Method to handle submission of viewing ticket information
        def submit_view_information():
            ticket_number_ = ticket_number.get()
            
            # If ticket number is empty, render an error box and return early
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

            # Close the input window
            input_window.destroy() 

        # Render submit button to submit ticket number and invoke the submit_view_information method
        submit_button = tk.Button(input_window, text="Submit", command=submit_view_information)
        submit_button.pack(pady=10)
        