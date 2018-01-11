import time
import csv

from pymouse import *
from pykeyboard import pykeyboard

class Student():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x+y)


a=Student(100,50)
print(time.ctime())

#csv_file=csv.reader(open(r'C:\Users\dengxinqiang\Desktop\csv.csv','r'))
#print(csv_file)

#for stu in csv_file:
 #   print(stu[2])


#stu=['aa','bb','cc']
#stu1=['11','22','33']
#打开文件
#out =open(r'C:\Users\dengxinqiang\Desktop\csv.csv','a',newline='')
#设定写入模式
#file_csv_write=csv.writer(out,dialect='excel')
#写入具体内容
#file_csv_write.writerow(stu)
#file_csv_write.writerow(stu1)
#print( '已写入' )

