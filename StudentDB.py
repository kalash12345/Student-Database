#importing dependencies
import os
import pandas as pd
import matplotlib.pyplot as plt

print('''         Welcome to Student Database and Management
            This program will help you to view your child's performance

Enter 1 : To Add a Data of a Class
Enter 2 : To Add Cycle Test 1 Marks
Enter 3 : To Add Cycle Test 2 Marks
Enter 4 : To Add Cycle Test 3 Marks
Enter 5 : To Add Cycle Test 4 Marks
Enter 6 : To View the data of all the students
Enter 7 : To View the performance of the students
Enter 8 : To Rename your file name
Enter 9 : To Exit the Program ''')

print()

#Enter your class(in roman numeral) with section - ALL CAPS
Class = input('Enter your Class : ')
Section = input('Enter your Section : ')
l = []
Add = []
DOB = []
transport = []
mail = []
M1 = []
M2 = []
M3 = []
M4 = []
dic = {}

#defining functions to feed the data

def Student():
    No_of_Students = int(input("Enter the total Students in your class :"))
    print()
    for i in range(No_of_Students):
        print()
        print('Enter Name' , i+1 , ':')
        name = input()
        l.append(name)
        print('Enter the Address :')
        add = input()
        Add.append(add)
        print('Enter DOB :')
        dob = input()
        DOB.append(dob)
        print('Transportation type :')
        trans = input()
        transport.append(trans)
        print('Email ID :')
        email = input()
        mail.append(email)

print()

def Marks1(): #Cycle Test 1 Marks
    print()
    print('Enter Cycle Test 1 Marks :')
    print()
    LB = int(input("Enter the Lower bond :"))
    UB = int(input("Enter the Upper bond :"))
    print()
    for i in range(LB,UB):
        Marks = float(input('Enter the Mark :'))
        M1.append(Marks)

def Marks2(): #Cycle Test 2 Marks
    print()
    print('Enter Cycle Test 2 Marks :')
    print()
    LB = int(input("Enter the Lower bond :"))
    UB = int(input("Enter the Upper bond :"))
    print()
    for i in range(LB,UB):
        Marks = float(input('Enter the Mark :'))
        M2.append(Marks)

def Marks3(): #Cycle Test 3 Marks
    print()
    print('Enter Cycle Test 3 Marks :')
    print()
    LB = int(input("Enter the Lower bond :"))
    UB = int(input("Enter the Upper bond :"))
    print()
    for i in range(LB,UB):
        Marks = float(input('Enter the Mark :'))
        M3.append(Marks)

def Marks4(): #Cycle Test 4 Marks
    print()
    print('Enter Cycle Test 4 Marks :')
    print()
    LB = int(input("Enter the Lower bond :"))
    UB = int(input("Enter the Upper bond :"))
    print()
    for i in range(LB,UB):
        Marks = float(input('Enter the Mark :'))
        M4.append(Marks)

def Statistics():
    print()
    print('Want to View the performance of your Child ? Choose any of the following options :','\n','\n','1.Average of the Class','\n','2.Statistics of the Class',
          '\n','3.Highest Mark in the Class','\n','4.Lowest Mark in the Class','\n','5.Statistics per Student in Cycle Test 1','\n',
          '6.Statistics per Student in Cycle Test 2','\n','7.Statistics per Student in Cycle Test 3','\n','8.Statistics per Student in Cycle Test 4','\n',
          '9.To Exit from Statistics')

    print()
    while True:
        y = int(input('What do you want to see ?'))
        print()
        if y == 1:
            print('Average of the Class is :')
            print()
            print(df[['Cycle Test 1','Cycle Test 2','Cycle Test 3','Cycle Test 4']].mean())
            print()
        elif y == 2:
            a = ['Cycle Test - 1','Cycle Test - 2','Cycle Test - 3','Cycle Test - 4']
            b = df[['Cycle Test 1','Cycle Test 2','Cycle Test 3','Cycle Test 4']].mean()
            print(b)
            plt.plot(a,b)
            plt.xlabel('Tests')
            plt.ylabel('Marks')
            plt.title('Average of Class')
            plt.show()
        elif y == 3:
            print('Highest Marks in the Class :')
            print()
            print(df[['Cycle Test 1','Cycle Test 2','Cycle Test 3','Cycle Test 4']].max())
            print()
        elif y == 4:
            print('Lowest Marks in the Class :')
            print()
            print(df[['Cycle Test 1','Cycle Test 2','Cycle Test 3','Cycle Test 4']].min())
            print()
        elif y == 5:
            a = df['Name']
            b = df['Cycle Test 1']
            print(b)
            plt.bar(a,b,color = 'b')
            plt.xlabel('Names')
            plt.ylabel('Marks')
            plt.title('Marks - Cycle Test 1')
            plt.show()
        elif y == 6:
            a = df['Name']
            b = df['Cycle Test 2']
            print(b)
            plt.bar(a,b,color = 'r')
            plt.xlabel('Names')
            plt.ylabel('Marks')
            plt.title('Marks - Cycle Test 2')
            plt.show()
        elif y == 7:
            a = df['Name']
            b = df['Cycle Test 3']
            print(b)
            plt.bar(a,b,color = 'g')
            plt.xlabel('Names')
            plt.ylabel('Marks')
            plt.title('Marks - Cycle Test 3')
            plt.show()
        elif y == 8:
            a = df['Name']
            b = df['Cycle Test 4']
            print(b)
            plt.bar(a,b,color = 'y')
            plt.xlabel('Names')
            plt.ylabel('Marks')
            plt.title('Marks - Cycle Test 4')
            plt.show()
        elif y == 9:
            break
        else:
            print('Invalid Choice')

#Main Statements [LOOP]
while True:
    print()
    x = int(input("Choose your Option :"))
    print()
    if x == 1:
        Student()
        dic = {'Name':l,'Class':Class,'Section':Section,'Address':Add,'BirthDate':DOB,'Transport':transport,'Email ID':mail}
        df = pd.DataFrame(dic)
        df = df.sort_values('Name')
        print()

    elif x == 2:
        Marks1()
        dic = {'Name':l,'Class':Class,'Section':Section,'Address':Add,'BirthDate':DOB,'Transport':transport,'Email ID':mail,'Cycle Test 1':M1}
        df = pd.DataFrame(dic)
        df = df.sort_values('Name')

    elif x == 3:
        Marks2()
        dic = {'Name':l,'Class':Class,'Section':Section,'Address':Add,'BirthDate':DOB,'Transport':transport,'Email ID':mail,'Cycle Test 1':M1,
               'Cycle Test 2':M2}
        df = pd.DataFrame(dic)
        df = df.sort_values('Name')

    elif x == 4:
        Marks3()
        dic = {'Name':l,'Class':Class,'Section':Section,'Address':Add,'BirthDate':DOB,'Transport':transport,'Email ID':mail,'Cycle Test 1':M1,
               'Cycle Test 2':M2,'Cycle Test 3':M3}
        df = pd.DataFrame(dic)
        df = df.sort_values('Name')

    elif x == 5:
        Marks4()
        dic = {'Name':l,'Class':Class,'Section':Section,'Address':Add,'BirthDate':DOB,'Transport':transport,'Email ID':mail,'Cycle Test 1':M1,
               'Cycle Test 2':M2,'Cycle Test 3':M3,'Cycle Test 4':M4}
        df = pd.DataFrame(dic)
        df = df.sort_values('Name')

    elif x == 6:
        print()
        print("You are viewing your child's data")
        print()
        print(df)

    elif x == 7:
        Statistics()

    elif x == 8:
        print('Do you want to rename your file name ? [y/n]')
        x = input('Choose your Option :')
        if x == 'y' or x == 'Y':
            Name = input('Enter the name with valid extension :')
            with open(Name,mode = 'w') as student_file:
                df.to_csv(Name)
                print('Your data has been saved with the above name')
        elif x == 'n' or x == 'N':
            print('Your data is saved with default name')
        else:
            print('Wrong Choice')

    elif x == 9:
        break

    else:
        print('Invalid Choice')
        
        
        
    
        























    
