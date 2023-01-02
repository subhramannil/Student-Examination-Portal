import csv
import os
path4='Department.csv'
if os.path.isfile(path4):
    pass
else:
    fob4=open('Department.csv','a')
    wob4=csv.writer(fob4)
    wob4.writerow(['Department ID','Department Name','List of batches'])
    fob4.close()
    
def dept():
    while True:
        print('a.Create a new Department')
        print('b.View all batches in a department')
        print('c.View average performance of all batches in a departmment')
        print('d.Show department statistics')
        print('e.EXIT')
        ch4=input('Enter your choice:')
        if ch4 in('a','A'):
            while True:
                fob4=open('Department.csv','r')
                rob4=csv.reader(fob4)
                l4a=[]
                sl4a=[]
                z=-1
                for row in rob4:
                    sl4a.append(row)
                a4=input('Enter Department ID:')
                b4=input('Enter Department Name:')
                c4=input('Enter Batch name:')
                l4a=[a4,b4,c4]
                try:
                    while True:
                        z+=1
                        if sl4a[z][2]!=c4:
                            pass
                        else:
                            while sl4a[z][2]==c4:
                                if sl4a[z]==l4a:
                                    print('This record already exists.')
                                    print('Enter again')
                                    c4=input('Enter Batch name:')
                                    z=-1
                                else:
                                    print('INVALID INPUT!!')
                                    print('One Batch Belongs to only one Department')
                                    print('Enter again')
                                    c4=input('Enter Batch name:')
                                    z=-1
                except IndexError:
                    fob4.close()
                    fob4=open('Department.csv','a',newline='')
                    wob4=csv.writer(fob4)
                    l4a=[a4,b4,c4]
                    wob4.writerow(l4a)
                    fob4.close()
                sch4=input('Enter more records(y/n):')
                if sch4 in('n','N'):
                    break
                fob4.close()
            fob4.close()
        elif ch4 in('b''B'):
            fob4=open('Department.csv','r')
            rob4=csv.reader(fob4)
            l4b=[]
            ask4b=input('Enter the department ID:')
            for row in rob4:
                if row==ask4b:
                    l4b.append(row[2])
            print('All The Batches in this Department are:')
            for i in l4b:
                print(i)
            print()
            print()
            fob4.close()
