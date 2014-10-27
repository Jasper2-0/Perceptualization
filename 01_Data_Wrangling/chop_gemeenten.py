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
            
            # weird edge case met Rozendaal...
            if data[i][j][3] == '-':
                data[i][j][3] = 0
            
            tree[gemeente][year][bracket] = float(data[i][j][3])
    
    return tree
    
# ==========================
# = Normalize by Age Group =
# ==========================
def normalizeByAgeGroup(tree):
     pass           
def normalizeByGemeente(tree):
    pass
def normalizeByCountry(tree):
    
    maxValue = 0.0
    minValue = 0.0

    
    for gemeente in sorted(tree):
        for year in sorted(tree[gemeente]):
            for ageGroup in sorted(tree[gemeente][year]):
                                
                value = tree[gemeente][year][ageGroup] 
                    
                if value > maxValue:
                    maxValue = value
                if value < minValue:
                    minValue = value
    
    
    result = []
            
    for gemeente in sorted(tree):
        
        l = {}
        
        l['name'] = gemeente;
        
        for ageGroup in tree['Amsterdam']['1988'].keys():
            l[ageGroup] = [];
            
        for year in sorted(tree[gemeente]):
            for ageGroup in sorted(tree[gemeente][year]):
                
                value = tree[gemeente][year][ageGroup]
                normValue = (value - minValue) / (maxValue - minValue)
                
                l[ageGroup].append((year,normValue))
        
        result.append(l)
        
    return result

def saveData(folderName,data):
    cwd = os.getcwd();
    targetDir = cwd+'/normalized/'+folderName;
    
    os.chdir(targetDir);
    
    for gemeente in data:
        os.mkdir(gemeente['name'])
        os.chdir(targetDir+'/'+gemeente['name']);
        
        for ageGroup in gemeente:
            if ageGroup != 'name':
                
                os.mkdir(ageGroup)
                os.chdir(targetDir+'/'+gemeente['name']+'/'+ageGroup)

                fo = open("values.txt","wb")
                
                for year in gemeente[ageGroup]:
                    line = year[0]+', '+str(year[1])+';\n'
                    fo.write(line)
                
                fo.close()
                
                os.chdir(targetDir+'/'+gemeente['name']);
        
        os.chdir(targetDir);
        
tree = buildTree(parseCSVFile(rawFile))
result = normalizeByCountry(tree)

saveData('byCountry',result)