import tkinter as tk
from tkinter import messagebox
import os
import csv

from booking_manager_gui import BookingManagerGUI
from constants import CSV_FILE
from constants import FILE_HEADERS

class AirlineReservationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation System")
        self.booking_manager = BookingManagerGUI()

        self.create_widgets()

        # Ensure CSV file exists with headers
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode='w', newline='') as db_write:
                writer = csv.writer(db_write)
                writer.writerow(FILE_HEADERS)

    def create_widgets(self):
        tk.Label(self.root, text="Airline Reservation System", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Main Menu", font=("Helvetica", 14)).pack(pady=5)

        tk.Button(self.root, text="1. Book a Ticket", width=25, command=self.booking_manager.book_ticket).pack(pady=5)
        tk.Button(self.root, text="2. Cancel a Ticket", width=25, command=self.booking_manager.cancel_ticket).pack(pady=5)
        tk.Button(self.root, text="3. View Available Seats", width=25, command=self.booking_manager.view_available_seats).pack(pady=5)
        tk.Button(self.root, text="4. Update Booking", width=25, command=self.booking_manager.update_booking).pack(pady=5)
        tk.Button(self.root, text="5. View Ticket Information", width=25, command=self.booking_manager.view_ticket_information).pack(pady=5)
        tk.Button(self.root, text="6. Exit", width=25, command=self.exit_app).pack(pady=10)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    AirlineReservationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()