import csv
import os
import random
#
#
# def custerid():
#     for i in range(0,10):
#         newrand = random.randrange(10)
#         print(newrand + i)


# custerid()

# function to initialise the csv file with header
FILENAME='cusid_db.csv'
def initialize_csv():
    #check if the file exists
    if not os.path.exists(FILENAME):
    #    If the file does not exist, create it and write as a header
    # try:
    #     with open(FILENAME,mode='r') as db_read:
    #         pass
    # except FileNotFoundError:
        with open(FILENAME,mode='w') as db_write:
            rows = csv.writer(db_write,delimiter=',',quoting=csv.QUOTE_MINIMAL)
            rows.writerow(['First Name','Last. Name','Customer ID','Ticket Number','Flight Time','Seat','Class','Status'])
initialize_csv()
# function to write into csv file (EXAMPLE WITH MY NAME)
# def write():
#     with open('cusid_db.csv', mode='w') as db_write:
#         rows = csv.writer(db_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#         # rows.writerow(['Marie-at','NLemvo','350','256789','6:00am','13F','economy','active'])
# #run the function first before reading
# write()
# function to read
with open ('cusid_db.csv', mode='r') as db_read:
    csv_reader = csv.reader(db_read, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {" | ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} ticket number {row[2]} customer id {row[3]} for the {row[4]} flight in seat {row[5]},{row[6]} Class, Status:{row[7]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
# Generate unique customer ID and ticket number
def generate_customer_id():
    return random.randint(100,999)
def generate_ticket_number():
    return f"{generate_customer_id()}-{random.randint(10000,99999)}"
# Function to book a ticket
def book_ticket(first_name,last_name,flight_time,seat,flight_class="economy"):
    customer_id = generate_customer_id()
    ticket_number = generate_ticket_number()
    status = 'active'

    with open(FILENAME,mode='a', newline='') as db_write:
        writer = csv.writer(db_write,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([first_name,last_name,customer_id,ticket_number,flight_time,seat,flight_class,status])

        print(f"Booking successful!Ticker Number:{ticket_number}, Seat:{seat}")


# # random number generator
#     def custerid():
#         for i in range(0, 10):
#             newrand = random.randrange(10)
#             print(newrand + i)




# function book ticket
#Define seat rows and allowed seat letters per class
UPPER_CLASS_ROWS = range(1,12)
PREMIUM_CLASS_ROWS = range (21,28)
ECONOMY_CLASS_ROWS = range (45,53)

#Seat letters allowed for each class
UPPER_CLASS_LETTERS = ['A','D','G','K']
PREMIUM_CLASS_LETTERS = ['A','C','D','E','F','G','H','K']
ECONOMY_CLASS_LETTERS = ['A','B','C','D','E','F','G','H','J','K']
# function to generate seats based on the row range and seat letters for each class used r instead of row
def generate_seats(row_range,seat_letters):
    return [f"{r}{letter}" for r in row_range for letter in seat_letters]
# Generate seats for each class based on the specified seat letters for each class
upper_class_seats = generate_seats(UPPER_CLASS_ROWS,UPPER_CLASS_LETTERS)
premium_class_seats= generate_seats(PREMIUM_CLASS_ROWS,PREMIUM_CLASS_LETTERS)
economy_class_seats= generate_seats(ECONOMY_CLASS_ROWS,ECONOMY_CLASS_LETTERS)

# combine all seats and limit to 100 seats/this caps the list
total_seats = upper_class_seats + premium_class_seats + economy_class_seats
limited_seats = total_seats[:100]
# function to assign a seat based on the requested class
def assign_seat(seat_class):
    if seat_class == 'upper':
        if upper_class_seats:
            seat = random.choice(upper_class_seats)
            upper_class_seats.remove(seat)
            return seat
        else:
            return "No Upper Class seats available."
    elif seat_class == 'premium':
        if premium_class_seats:
            seat = random.choice(premium_class_seats)
            premium_class_seats.remove(seat)
            return seat
        else:
            return "No Premium Class seats available."
    elif seat_class == 'economy':
        if economy_class_seats:
            seat = random.choice(economy_class_seats)
            economy_class_seats.remove(seat)
            return seat
        else:
            return "No Economy Class seats available."
    else:
        return "Invalid class selection."
# Print available seats in each class for verification
print("Initial Upper Class Seats:", len(upper_class_seats))
print("Initial Premium Class Seats:", len(premium_class_seats))
print("Initial Economy Class Seats:", len(economy_class_seats))

#Example booking process
def book_seat(seat_class):
    seat = assign_seat(seat_class)
    if "available" not in seat:
        class_display = seat_class.capitalize() if seat_class.lower() !="upper" else "Upper"
        print(f"Seat{seat} sucessfully booked in {class_display} Class.")
    else:
        print(seat) #This will display if no seats are available in the chosen class

#Simulate bookings
book_seat('upper')
book_seat('premium')
book_seat('economy')
book_seat('upper') #attempt to book another upper class seat

# Print remaining seats after booking attempts
print("Remaining Upper Class Seats:", len (upper_class_seats))
print("Remaining Premium Class Seats:",len(premium_class_seats))
print("Remaining Economy Class Seats:",len(economy_class_seats))

# function cancel ticket
# function update ticket