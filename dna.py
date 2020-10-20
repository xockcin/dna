import sys
import csv

if not len(sys.argv) == 3:  # if there aren't exactly three arguments
    print("Usage: dna.py [database] [sequence]")  # print error message
    quit()

database_file = open(sys.argv[1])  # open database and sequence files
sequence_file = open(sys.argv[2])  # from command line

database = csv.DictReader(database_file)  # read database into csv reader
sequence = sequence_file.read()  # read sequence into string

item_list = database.fieldnames[1:]  # list of STR's, with "name" removed

data = {}  # initialize data dictionary
for item in item_list:  # set each key to zero
    data[item] = 0

position = 0  # start at the beginning of the sequence
while position < len(sequence):  # until the end of the sequence
    for item in item_list:  # for each STR in the list
        count = 0  # start a count
        while sequence[position:].startswith(item*(count+1)):  # where the magic happens
            count += 1  # count one STR
        if count > data[item]:  # after the run ends, if it was the biggest yet
            data[item] = count  # record it in the dictionary
    position += 1  # advance one position forward
    
for row in database:  # for each row in person database
    current = [int(row[item]) for item in item_list]  # make a list of that persons STR counts
    if current == list(data.values()):  # if it's the same as the list from our data
        print(row['name'])  # print the person's name
        quit()

print('No match')
