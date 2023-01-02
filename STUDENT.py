import csv
import os
path1='Student.csv'
if os.path.isfile(path1):
    pass
else:
    fob1=open('Student.csv','a')
    wob1=csv.writer(fob1)
    wob1.writerow(['Student ID','Name','Class Roll No.','Batch ID'])
    fob1.close()
    def help(d4,l3a6):
    if d4 in l3a6:
        print('This Student already exists!')
        print('Enter again')
        d4=input('Student ID:')
        help(d4,l3a6)
        
        
def help1(num):
    var='PASS'
    if num>=90:
        grade='A'
    elif num>=80 and num<90:
        grade='B'
    elif num>=70 and num<80:
        grade='C'
    elif num>=60 and num<70:
        grade='D'
    elif num>=40 and num<60:
        grade='E'
    elif num<40:
        grade='F'
        var='FAIL'
    return(var,grade)


def student():
    while True:
        print('a.Create a new student')
        print('b.Update student details')
        print('c.Remove a student from the database')
        print('d.Generate report card')
        print('e.Exit')
        ch1=input('Enter your choice:')
        if ch1 in ('a','A'):
            while True:
                l1a1,l1a2=[],[]
                a1=input('Enter Student ID:')
                fob1=open('Student.csv','r')
                rob1=csv.reader(fob1)
                for row in rob1:
                    l1a1.append(row)
                fob1.close()
                for i in range(len(l1a1)):
                    l1a2.append(l1a1)
                while True:
                    if a1 in l1a2:
                        print('This student already exists')
                        print('Enter again')
                        a1=input('Enter Student ID:')
                    else:
                        break
                b1=input('Enter name of the Student:')
                c1=input('Enter class roll number:')
                d1=input('Enter Batch ID:')
                fob1=open('Student.csv','a',newline='')
                wob1=csv.writer(fob1)
                wob1.writerow([a1,b1,c1,d1])
                fob1.close()
                sch1=input('Enter more records?(y/n):')
                if sch1 in ('n','N'):
                    break
        elif ch1 in('b','B'):
            while True:
                l1b1=[]
                ask1b1=input('Enter the Student ID of the student whose details you want to update:')
                fob1=open('Student.csv','r')
                rob1=csv.reader(fob1)
                for row in rob1:
                    l1b1.append(row)
                fob1.close()
                for i in range(len(l1b1)):
                    if l1b1==ask1b1:
                        del l1b1[i]
                        break
                fob1=open('Student.csv','w')
                fob1.truncate()
                fob1.close()
                fob1=open('Student.csv','w',newline='')
                wob1=csv.writer(fob1)
                wob1.writerows(l1b1)
                fob1.close()
                b1b=input('Enter name of the Student:')
                c1b=input('Enter class roll number:')
                d1b=input('Enter Batch ID:')
                fob1=open('Student.csv','a',newline='')
                wob1=csv.writer(fob1)
                wob1.writerow([ask1b1,b1b,c1b,d1b])
                fob1.close()
                sch2=input('Update more records?(y/n)')
                if sch2 in ('n','N'):
                    break
        elif ch1 in ('c','C'):
            while True:
                l1c1=[]
                ask1c1=input('Enter the Student ID of the student whose details you want to delete:')
                fob1=open('Student.csv','r')
                rob1=csv.reader(fob1)
                for row in rob1:
                    l1c1.append(row)
                fob1.close()
                for i in range(len(l1c1)):
                    if l1c1==ask1c1:
                        del l1c1[i]
                        break
                fob1=open('Student.csv','w')
                fob1.truncate()
                fob1.close()
                fob1=open('Student.csv','w',newline='')
                wob1=csv.writer(fob1)
                wob1.writerows(l1c1)
                fob1.close()
                sch3=input('Delete more records?(y/n)')
                if sch3 in ('n','N'):
                    break
        elif ch1 in('d','D'):
            while True:
                l1d1,l1d2=[],[]
                print('Enter Student ID of the student whose report is to be generated')
                with open('Examination.csv','r') as fob5, open('result.txt','w+') as res:
                    rob5=csv.reader(fob5)
                    a1d=input('Student ID:')
                    for row in rob5:
                        if row==a1d:
                            l1d1=row
                    z=int(l1d1[1])+int(l1d1[2])+int(l1d1[3])+int(l1d1[4])+int(l1d1[5])
                    y=z/5
                    a1d1=help1(int(l1d1[1]))
                    a1d2=help1(int(l1d1[2]))
                    a1d3=help1(int(l1d1[3]))
                    a1d4=help1(int(l1d1[4]))
                    a1d5=help1(int(l1d1[5]))
                    a1d6=help1(y)
                    l1d2=['Student ID: '+a1d+'\n','Percentage of student: '+str(y)+'%\n','Grade in Physics: '+a1d1[1]+'\n','Grade in Chemistry: '+a1d2[1]+'\n','Grade in Math=: '+a1d3[1]+'\n','Grade in English: '+a1d4[1]+'\n','Grade in Computer: '+a1d5[1]+'\n','Passing Status:'+a1d6[0]]
                    res.write('REPORT CARD\n')
                    res.writelines(l1d2)
                res=open('result.txt','r')
                print(res.read())
                res.close()
                sch6=input('Generate more report cards?(y/n):')
                if sch6 in ('n','N'):
                    break
        elif ch1 in('e','E'):
            break
        else:
            print('INVALID INPUT!!')
            print('Enter again')
