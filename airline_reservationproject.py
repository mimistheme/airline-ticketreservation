import csv
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
            print(f'\t{row[0]} {row[1]} ticket number {row[2]} customer id {row[3]} for the {row[4]} flight in seat {row[5]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
      # booking a seat
    


