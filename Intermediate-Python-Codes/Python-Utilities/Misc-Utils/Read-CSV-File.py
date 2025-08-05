import csv

# pip install pandas 

"""
With Syntax is better cause here we don't need to worry about closing the file, 
it gets closed automatically after the block ends
"""


with open('data\\Movie-Series-Characters.csv' ) as csvFile:
    # csvReader = csv.reader( csvFile, delimiter=',')
    csvReader = csv.reader(csvFile)

    for row in csvReader:
        print( row[0], '\t\t', row[1], '\t\t\t', row[2], '\t\t\t\t', row[3] )
        # print( '\t\t\t\t'.join(row) )

print( '\n Properly formatted Output with Pandas:' )
#
import pandas as pd

df = pd.read_csv('data\\Movie-Series-Characters.csv')
# print( df.columns[4] )
# Drop the Last column as it's empty
df = df.drop( df.columns[4], axis=1)
print( df )

