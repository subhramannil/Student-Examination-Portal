import csv
import os
path3='Batch.csv'
if os.path.isfile(path3):
    pass
else:
    fob3=open('Batch.csv','a')
    wob3=csv.writer(fob3)
    wob3.writerow(['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
    fob3.close()
    def batch():
    while True:
        print('a.Create a new batch')
        print('b.View list of all students in a batch')
        print('c.View list of all courses taught in the batch')
        print('d.View complete performance of all students in a batch')
        print('e.Pie chart of percentage of all students')
        print('f.EXIT')
        ch3=input('Enter your choice:')
        if ch3 in ('a','A'):
            while True:
                l3a1,l3a2,l3a3,l3a5,l3a6=[],[],[],[],[]
                fob3=open('Batch.csv','r')
                rob3=csv.reader(fob3)
                for row in rob3:
                    l3a5.append(row)
                for m in range(len(l3a5)):
                    l3a6.append(l3a5)
                fob3.close()
                a3=input('Enter Batch ID:')
                b3=input('Enter Batch Name:')
                c3=input('Enter Department Name:')
                ask3a1=int(input('Enter the number of courses in the batch:'))
                ask3a2=int(input('Enter the numner of students in the batch:'))
                for i in range(ask3a1):
                    c4=input('Enter Course ID of No.{i+1}:')
                    l3a1.append(c4)
                for j in range(ask3a2):
                    d4=input('Enter Student ID of No.{j+1}:')
                    while True:
                        if d4 in l3a6:
                            print('This Student already exists!')
                            print('Enter again')
                            d4=input('Student ID:')
                            help(d4,l3a6)
                        else:
                            break
                    l3a2.append(d4)
                for k in l3a1:
                    for l in l3a2:
                        l3a4=[a3,b3,c3,k,l]
                        l3a3.append(l3a4)
                fob3=open('Batch.csv','a',newline='')
                wob3=csv.writer(fob3)
                wob3.writerows(l3a3)
                fob3.close()
                sch3=input('Enter more records?(y/n):')
                if sch3 in ('n','N'):
                    break
        elif ch3 in('b','B'):
            l3b1,l3b2=[],[]
            fob3=open('Batch.csv','r')
            rob3=csv.reader(fob3)
            for row in rob3:
                l3b1.append(row)
            fob3.close()
            ask3b1=input('Enter the required batch ID:')
            for i in range(len(l3b1)):
                if l3b1==ask3b1:
                    l3b2.append(l3b1)
            l3b3=list(set(l3b2))
            l3b3.sort()
            print('The students enrolled in the given batch are:')
            for j in l3b3:
                print(j)
        elif ch3 in('c','C'):
            l3c1,l3c2=[],[]
            fob3=open('Batch.csv','r')
            rob3=csv.reader(fob3)
            for row in rob3:
                l3c1.append(row)
            fob3.close()
            ask3c1=input('Enter the required batch ID:')
            for i in range(len(l3c1)):
                if l3c1==ask3c1:
                    l3c2.append(l3c1)
            l3c3=list(set(l3c2))
            l3c3.sort()
            print('The list of all courses taught in the batch:')
            for j in l3c3:
                print(j)
            print()
            print()
