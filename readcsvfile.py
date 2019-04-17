import csv

file_name='books.csv'

with open(file_name,newline='')as csvf:
    csv_reader=csv.reader(csvf)
    for row in csv_reader:
        print(row)
