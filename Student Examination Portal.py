# Student Examination Portal
#import csv
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


path2='Course.csv'
if os.path.isfile(path2):
    pass
else:
    fob2=open('Course.csv','a')
    wob2=csv.writer(fob2)
    wob2.writerow(['Course ID','Course Name','Student ID','Marks Obtained'])
    fob2.close()


path3='Batch.csv'
if os.path.isfile(path3):
    pass
else:
    fob3=open('Batch.csv','a')
    wob3=csv.writer(fob3)
    wob3.writerow(['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
    fob3.close()


path4='Department.csv'
if os.path.isfile(path4):
    pass
else:
    fob4=open('Department.csv','a')
    wob4=csv.writer(fob4)
    wob4.writerow(['Department ID','Department Name','List of batches'])
    fob4.close()

path5='Examination.csv'
if os.path.isfile(path5):
    pass
else:
    fob5=open('Examination.csv','a')
    wob5=csv.writer(fob5)
    wob5.writerow(['Student ID','Physics','Chemistry','Math','English','Computer'])
    fob5.close()

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


def course():
    while True:
        print('a.Create a new course')
        print('b.View performance of all students in the course')
        print('c.Show course statistics')
        print('d.Exit')
        ch2=input('Enter your choice:')
        if ch2 in ('a','A'):
            while True:
                l2a2,l2a3,l2a4=[],[],[]
                a2=input('Enter Course ID:')
                b2=input('Enter Course Name:')
                fob2=open('Course.csv','r')
                rob2=csv.reader(fob2)
                for row in rob2:
                    if row==a2:
                        l2a2.append(row[2])
                fob2.close()
                ask2a1=int(input('Enter the number of students in the course:'))
                for i in range(ask2a1):
                    c2=input("Student ID of no.{i+1}: ")
                    while True:
                        if c2 in l2a2:
                            print('This Student already exists in this course!')
                            print('Enter again')
                            c2=input('Student ID:')
                            help(c2,l2a2)
                        else:
                            break
                    d2=int(input('Enter the Total marks:'))
                    l2a3.append([c2,d2])
                for l in range(len(l2a3)):
                    l2a4.append([a2,b2,l2a3[l][0],l2a3[l][1]])
                fob2=open('Course.csv','a',newline='')
                wob2=csv.writer(fob2)
                wob2.writerows(l2a4)
                fob2.close()
                sch2=input('Enter more Courses?(y/n):')
                if sch2 in ('n','N'):
                    break
        elif ch2 in('b','B'):
            while True:
                l2b1,l2b2,l2b3,l2b4,l2b5,l2b6,l2b7=[],[],[],[],[],[],[]
                a2=input('Enter course ID:')
                with open('Course.csv','r') as fob2b1 , open('Examination.csv','r') as fob2b2 , open('Student.csv','r') as fob2b3:
                    rob2b1=csv.reader(fob2b1)
                    rob2b2=csv.reader(fob2b2)
                    rob2b3=csv.reader(fob2b3)
                    for row1 in rob2b1:
                        if row1==a2:
                            l2b1.append(row1[2])
                    for row2 in rob2b2:
                        l2b2.append(row2)
                        l2b4.append(row2)
                    for row3 in rob2b3:
                        l2b3.append(row3)
                        l2b5.append(row3)
                for i in range(len(l2b1)):
                    if l2b1[i] in l2b4 and l2b1[i] in l2b5:
                        for j in range(len(l2b3)):
                            if l2b1==l2b3:
                                l2b6.append([l2b3[j][1],l2b3[j][2]])
                for k in range(len(l2b1)):
                    if l2b1[k] in l2b4 and l2b1[k] in l2b5:
                        for l in range(len(l2b2)):
                            if l2b1==l2b2:
                                l2b7.append([l2b2[l][1],l2b2[l][2]],l2b2[l][3],l2b2[l][4],l2b2[l][5])
                for m in range(len(l2b1)):
                    print('Student No.{m+1}')
                    print('Student ID:',l2b1[m])
                    print('Name:',l2b6[m][0])
                    print('Class Roll No.',l2b6[m][1])
                    print('Marks in Physics:',l2b7[0])
                    print('Marks in Chemistry:',l2b7[1])
                    print('Marks in Math:',l2b7[2])
                    print('Marks in English:',l2b7[3])
                    print('Marks in Computer:',l2b7[4],'\n')
                                    
                                                                                                            
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

            
def exam():
    while True:
        l5a1=[]
        a5=input('Enter student ID:')
        fob5=open('Examination.csv','r')
        rob5=csv.reader(fob5)
        for row in rob5:
            l5a1.append(row)
        fob5.close()
        while True:
            if a5 in l5a1:
                print('This student already exists')
                print('Enter again')
                a5=input('Enter student ID:')
            else:
                break
        print('Enter marks in the subjects:')
        b5=input('Physics')
        c5=input('Chemistry')
        d5=input('Math')
        e5=input('English')
        f5=input('Computer')
        fob5=open('Examination.csv','a',newline='')
        wob5=csv.writer(fob5)
        wob5.writerow([a5,b5,c5,d5,e5,f5])
        fob5.close()
        sch5=input('Enter more records?(y/n)')
        if sch5 in ('n','N'):
            break
        
        
while True:
    print('1.Student Details')
    print('2.Course Details')
    print('3.Batch Details')
    print('4.Department Details')
    print('5.Examination Details')
    print('6.END')
    ch=int(input('Enter your choice:'))
    if ch==1:
        student()
    elif ch==2:
        course()
    elif ch==3:
        batch()
    elif ch==4:
        dept()
    elif ch==5:
        exam()
    elif ch==6:
        break
    else:
        print('INVALID INPUT!!')
        print('Enter again')
