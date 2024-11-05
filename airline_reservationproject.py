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
# function to write into csv file
def write():
    with open('cusid_db.csv', mode='w') as db_write:
        rows = csv.writer(db_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        rows.writerow(['Marie-at','NLemvo','350','256789','6:00am','13n','economy','active'])
#run the function first before reading
write()
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

        print(f"Booking successul!Ticker Number:{ticket_number}, Seat:{seat}")
# # random number generator
#     def custerid():
#         for i in range(0, 10):
#             newrand = random.randrange(10)
#             print(newrand + i)




# function book ticket
# function cancel ticket
# function update ticket