import csv
# function to write into csv file
def write():
    with open('customerid_db.csv', mode='w') as db_write:
        rows = csv.writer(db_write, delimiter=',', quoting=csv.QUOTE_MINIMAL, qoutechar='"')
        rows.writerow(['Marie','NLemvo','350','256789','6:00am','13n','economy','active'
])
# function to read
with open ('customerid_db.csv', mode='r') as db_read:
    pass
