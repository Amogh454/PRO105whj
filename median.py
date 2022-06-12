import csv
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

newData.sort()

if n%2==0:
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1+m2)/2

else:
    median = newData[n//2]    

print(median)    








