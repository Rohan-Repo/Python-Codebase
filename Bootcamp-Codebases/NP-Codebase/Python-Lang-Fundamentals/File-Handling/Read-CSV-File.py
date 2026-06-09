import csv

# Read CSV using Default CSV Library 
with open('transactions.csv' ) as csvFile:
    # csvReader = csv.reader( csvFile, delimiter=',')
    csvReader = csv.reader(csvFile)

    for row in csvReader:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4], '\t', row[5], '\t', row[6], '\t', row[7])