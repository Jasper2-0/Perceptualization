import os
import csv
import sys 

reload(sys) 
sys.setdefaultencoding("utf-8")

rawFile = 'raw/Bevolking__leeftijd,_191014225304.csv'
testFile = 'raw/test.csv'


# =======================================================
# = Parse our CSVFile into more managable inside python =
# =======================================================

def parseCSVFile(csvFile):
    data = []
    rows = []
    
    # parse csv file into a list
    with open(csvFile,'rb') as csvfile:
         reader = csv.reader(csvfile, delimiter=';')
    
         gemeente = ''
         rowCount = 0;
         for row in reader:
             if rowCount > 3:
                 if gemeente != row[0]:
                     data.append(rows)
                     rows = []
                 if row[3] != "":
                     rows.append(row)
                 gemeente = row[0]
             rowCount = rowCount +1
    
    # pop off the first empty list item
    data.pop(0)
    
    return data

# ==================================================
# = Build a tree datastructure from our parsed csv =
# ==================================================
def buildTree(data):
    
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
            tree[gemeente][year][bracket] = float(data[i][j][3])
    
    return tree
    
# ==========================
# = Normalize by Age Group =
# ==========================
def normalizeByAgeGroup(tree):

    maxValue = 0.0
    minValue = 0.0

    
    for gemeente in sorted(tree):
        
        print gemeente
        
        
        for year in sorted(tree[gemeente]):
            
            for ageGroup in sorted(tree[gemeente][year]):
                                
                value = tree[gemeente][year][ageGroup] 
                    
                if value > maxValue:
                    maxValue = value
                if value < minValue:
                    minValue = value
            
    for gemeente in sorted(tree):
        for year in sorted(tree[gemeente]):
            for ageGroup in sorted(tree[gemeente][year]):
                
                value = tree[gemeente][year][ageGroup]
                normValue = (value - minValue) / (maxValue - minValue)
                
                print normValue 
                
        
        #
        #
        #     if tree[gemeente][year]['Jonger dan 10 jaar'] != "":
        #         values.append((year,float(tree[gemeente][year]['Jonger dan 10 jaar'])))
        #
        # maxValue = 0;
        # minValue = 0;
        #
        # for value in values:
        #      if value[1] > maxValue:
        #          maxValue = value[1]
        #
        #      if value[1] < minValue:
        #          minValue = value[1]
        #
        # normalizedValues = []
        #
        # for value in values:
        #     normValue = (value[1] - minValue) / (maxValue - minValue)
        #     normalizedValues.append((value[0],normValue))
        #
        # print normalizedValues
    
def normalizeByGemeente(tree):
    pass
def normalizeByCountry(tree):
    pass

tree = buildTree(parseCSVFile(testFile))

#print tree

normalizeByAgeGroup(tree)