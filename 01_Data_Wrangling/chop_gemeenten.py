import os
import csv

rawFile = 'raw/Bevolking__leeftijd,_191014225304.csv'
testFile = 'raw/test.csv'

with open(testFile,'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';',)
    
    rowCount = 0;
    
    
    currentCity = '';
    currentYear = '';
    currentGroup = '';
    currentValue = '';
    
    for row in csvreader:
        if rowCount > 3:
            print row
            currentCity = row[0]
            currentYear = row[1]
            currentGroup = row[2]
            currentValue = row[3]
            
        rowCount = rowCount+1