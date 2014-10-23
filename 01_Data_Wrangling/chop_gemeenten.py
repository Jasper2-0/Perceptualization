import os
import csv

rawFile = 'raw/Bevolking__leeftijd,_191014225304.csv'
testFile = 'raw/test.csv'

data = []
rows = []

with open(testFile,'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=';')


     gemeente = ''
     rowCount = 0;
     for row in reader:
         if rowCount > 3:
             if gemeente != row[0]:
                 data.append(rows)
                 rows = []
                 
             rows.append(row)
             gemeente = row[0]
         rowCount = rowCount +1

data.pop(0)         
tree = {}


for i in range(len(data)):
    gemeente = data[i][0][0]
    tree[gemeente] = {}
    
    for j in range(len(data[i])):
        
        year = data[i][j][1]
        tree[gemeente][year] = {}
        
    for j in range(len(data[i])):
        year = data[i][j][1]
        bracket = data[i][j][2]
        tree[gemeente][year][bracket] = data[i][j][3]


for gemeente in tree:
    for year in tree[gemeente]:
        print tree[gemeente][year]