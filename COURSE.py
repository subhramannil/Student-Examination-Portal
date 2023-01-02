import csv
import os
path2='Course.csv'
if os.path.isfile(path2):
    pass
else:
    fob2=open('Course.csv','a')
    wob2=csv.writer(fob2)
    wob2.writerow(['Course ID','Course Name','Student ID','Marks Obtained'])
    fob2.close()
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
