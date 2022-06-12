import csv
import statistics

with open('data.csv',newline = '') as f:
    r=csv.reader(f)
    fileData = list(r)

fileData.pop(0)  

newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

n = len(newData)