class Reservation:
    def __init__(self, first_name, last_name, customer_id, ticket_num, seat, booking_time):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.ticket_num = ticket_num
        self.seat = seat
        self.booking_time = booking_time

    def print_reservation_details(self, current_bookings):
        remaining_seats = 100 - len(current_bookings) - 1
        print(f"\nCreated reservation for {self.first_name} {self.last_name} at {self.booking_time.strftime("%Y-%m-%d %H:%M:%S")}")
        print(f"The reservation number is {self.ticket_num} and the seat assigned is {self.seat}")
        print(f"There are now {remaining_seats} seats remaining\n")
