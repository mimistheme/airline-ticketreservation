# Class used to store information about a booking
class Reservation:
    def __init__(self, first_name, last_name, customer_id, ticket_num, seat, booking_time):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.ticket_num = ticket_num
        self.seat = seat
        self.booking_time = booking_time


    # Prints out all information related to a booking
    def print_reservation_details(self):
        print("\n-------------------------")
        print("   RESERVATION DETAILS")
        print("-------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Ticket Number: {self.ticket_num}")
        print(f"Seat Number: {self.seat}")
        print(f"Reservation booking date: {self.booking_time}\n")


    # Converts the reservation to a list so it can be written to the csv file in the correct format
    def to_csv_row(self):
        return [self.first_name, self.last_name, self.customer_id, self.ticket_num, self.seat, self.booking_time]
