import csv
import os
path5='Examination.csv'
if os.path.isfile(path5):
    pass
else:
    fob5=open('Examination.csv','a')
    wob5=csv.writer(fob5)
    wob5.writerow(['Student ID','Physics','Chemistry','Math','English','Computer'])
    fob5.close()
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
