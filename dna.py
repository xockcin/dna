
# Title: dna.py

# Author: xockcin

# Context: Written for a CS50 problem set
# cf: cs50.harvard.edu/x/2020/psets/6/dna/

# Purpose: To identify a given stequence of
# DNA as belonging to a particular person.

# Explanation: Our DNA is really nothing more
# than four different nucleotides, represented 
# as the letters G, A, T and C arranged in a
# particular sequence. In DNA there are certain
# common patterns called STRs, usually between
# 4 and 12 or so nucleotides long, that repeat
# over and over a specific number times in a
# person's genome. These STR repetitions are
# hightly specific to each individual, and are 
# a common way to identify DNA samples, as in
# forensic investigation.
#
# This program takes as inputs a database of
# STR profiles and a DNA sequence. The database
# is a CSV file with the STRs in the first row,
# people's names in the first column, and the 
# STR counts in the subsequent rows and columns.
# The sequence, a txt file, is simply a string:
# a long seqence of G's, A's, T's and C's.
#
# The program iterates through the sequence,
# finding and tallying each occurrence of a
# repeated STR in the sequence, keeping the
# tally only if it is the biggest one yet.
# Then it looks in the database for a match.

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
        if count > 0:
            position += count*len(item) - 2  # for speed, skip ahead to end of run        
        if count > data[item]:  # after the run ends, if it was the biggest yet
            data[item] = count  # record it in the dictionary
    position += 1  # advance one position forward
    
for row in database:  # for each row in person database
    current = [int(row[item]) for item in item_list]  # make a list of that person's STR counts
    if current == list(data.values()):  # if it's the same as the list from our data
        print(row['name'])  # print the person's name
        quit()

print('No match')
