def create_database():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger')
     y = x.cursor()
     x.autocommit = True
     y.execute("create database railways")
#create_database()

def railway_table():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger',database='railways')
     y = x.cursor()
     x.autocommit = True
     l = "create table railway(user_id int(10) primary key,name varchar(100),phno varchar(15),age int(3),gender char(1),from_f varchar(100),to_t varchar(100),date_d varchar(20),train_no int(5),time varchar,category varchar(10),seat_no int)"
     y.execute(l)
#railway_table()

def user_table():
    import mysql.connector as s
    x = s.connect(host='localhost',user='root',password='tiger',database='railways')
    y = x.cursor()
    x.autocommit = True
    l = "create table user(user_id int(10) primary key,firstname varchar(50),lastname varchar(50),password varchar(10),phno varchar(15),age int,gender char(1),dob varchar(20))"
    y.execute(l)
#user_table()

def menu():
     x = 1
     while x == 1:
          print("\nWELCOME TO ONLINE RAILWAY BOOKING")
          print("1.Log In")
          print("2.Sign Up")
          print("3.Delete Account")
          print("4.Exit")
          y = int(input("Enter your choice: "))
          if y == 1:
               a = checking()
               if a == True:
                    print("WELCOME")
                    main()
               else:
                    continue
          elif y == 2:
               a = checking_1()
               if a == True:
                    main()
               else:
                    continue
          elif y == 3:
               a = checking_2()
               if a == True:
                    print("Account successfully deleted")
                    continue
               else:
                    print("Your user_id or password is incorrect")
                    continue
          elif y == 4:
               print("THANK YOU for using our services!")
               break
          else:
               print("Enter valid input")
          print("1.Yes")
          print("2.No")
          x = int(input("Do you want to continue? \n"))

def main():
     x = 1
     while x == 1:
          print("1.Ticket Booking")
          print("2.Ticket Checking")
          print("3.Ticket Cancelling")
          print("4.Account Details")
          print("5.Log Out")
          y = int(input("Enter your choice: "))
          if y == 1:
               ticket_booking()
          elif y == 2:
               ticket_checking()
          elif y == 3:
               ticket_cancelling()
          elif y == 4:
               checking_3()
          elif y == 5:
               print("THANK YOU!")
               break
          else:
               print("Enter valid input")
          print("1.Yes")
          print("2.No")
          x = int(input("Do you want to continue? \n"))

def ticket_booking():
    import mysql.connector as s
    x=s.connect(host='localhost',user='root',password='tiger',database='railways')
    y=x.cursor()
    x.autocommit = True
    a = int(input("Enter your ID: "))
    b = input("Enter your name: ")
    c = input("Enter your phone no.: ")
    d = int(input("Enter your age: "))
    print("M = Male","\n","F = Female")
    e = input("Enter your gender: ")
    f = input("Enter your starting point: ")
    g = input("Enter your destination: ")
    day = input("Enter the day(DD): ")
    month = input("Enter the month(MM): ")
    year = input("Enter the year(YYYY): ")
    h = day+"/"+month+"/"+year
    seat = list(seat_checking(h,f,g))
    if seat[0] == True:
        l = "insert into railway values({},'{}','{}',{},'{}','{}','{}','{}',{},'{}','{}',{})".format(a,b,c,d,e,f,g,h,seat[1],seat[2],seat[3],seat[4])
        y.execute(l)
    else:
        pass
        

def ticket_checking():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger',database='railways')
     y = x.cursor()
     x.autocommit = True
     m = input("Enter your user_id: ")
     try:
         n = "select * from railway where user_id = '{}'".format(m)
         y.execute(n)
         data = y.fetchall()
         if data == []:
              print("NO RECORD FOUND!")
         for i in data:
              print("NAME: ",i[1])
              print("PHONE NUMBER: ",i[2])
              print("AGE: ",i[3])
              print("GENDER: ",i[4])
              print("STARTING POINT: ",i[5])
              print("DESTINATION: ",i[6])
              print("DATE: ",i[7])
              print("TRAIN NO.:",i[8])
              print("TIME: ",i[9])
              print("CATEGORY: ",i[10])
              print("SEAT NO.: ",i[11])
              print("\n")
     except:
          print("NO RECORD FOUND!")

def ticket_cancelling():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger',database='railways')
     y = x.cursor()
     x.autocommit = True
     m = input("Enter the user_id: ")
     a = int(input("Do you really want to cancel your ticket?\n"+"1.Yes\n"+"2.No\n"))
     if a == 1:
         l = "delete from railway where user_id = '{}'".format(m)
         y.execute(l)
         print("TICKET CANCELLED")
     else:
          pass
          

def checking():
    import mysql.connector as s
    x = s.connect(host='localhost',user='root',password='tiger',database='railways')
    y = x.cursor()
    x.autocommit = True
    a = int(input('USER ID: '))
    b = input('PASS WORD: ')
    try:
        m = "select user_id from user where password = '{}'".format(b)
        n = "select firstname,lastname from user where password = '{}'".format(b)
        y.execute(n)
        l = list(y.fetchall()[0])
        name = l[0] + ' ' + l[1]
        y.execute(m)
        l1 = list(y.fetchall()[0])[0]
        print(l1)
        if l1 == a:
             print('\nHELLO',name)
             return True
        else:
             print("Account does not exist.")
             return False
    except:
        print("ENTER CORRECT USERNAME OR PASSWORD")

def checking_1():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger',database='railways')
     y = x.cursor()
     x.autocommit = True
     a = int(input("\nUSER ID: "))
     b = input("FIRST NAME: ")
     c = input("LAST NAME: ")
     d = input("PASSWORD: ")
     e = input("RE-ENTER YOUR PASSWORD: ")
     while e != d:
          print("Enter correct password")
          e = input("RE-ENTER YOUR PASSWORD: ")
          if e == d:
               break
     f = input("PHONE NUMBER: ")
     g = int(input("AGE: "))
     print("M = Male","\n","F = Female")
     h = input("ENTER YOUR GENDER: ")
     i = input("ENTER YOUR DATE OF BIRTH(DD/MM/YYYY): ")
     try:
          l = "insert into user values({},'{}','{}','{}','{}',{},'{}','{}')".format(a,b,c,d,f,g,h,i)
          y.execute(l)
          print("\nWELCOME",b,c)
          return True
     except:
          print("USER_ID ALREADY EXISTS")
          return False
          
def checking_2():
     import mysql.connector as s
     x = s.connect(host='localhost',user='root',password='tiger',database='railways')
     y = x.cursor()
     x.autocommit = True
     a = int(input("USER_ID: "))
     b = input("PASS WORD: ")
     try:
          l = "select user_id from user where password='{}'".format(b)
          y.execute(l)
          data = list(y.fetchall()[0])
          if data[0] == a:
               l = "select * from user where password='{}'".format(b)
               y.execute(l)
               data = list(y.fetchall()[0])
               print("USER_ID: ",data[0])
               print("FIRST NAME: ",data[1])
               print("LAST NAME: ",data[2])
               print("PHONE NO.: ",data[4])
               print("AGE: ",data[5])
               print("GENDER: ",data[6])
               print("DOB: ",data[7])
               print("\n")
               print("1.Yes","\n","2.No")
               p = int(input("Do you really want to delete your account?"))
               if p == 1:
                    l = "delete from user where password = '{}'".format(b)
                    y.execute(l)
                    return True
               elif p == 2:
                    pass
               else:
                    print("ENTER VALID INPUT")
          else:
               return False
     except:
          print("ACCOUNT DOES NOT EXIST")

def checking_3():
    import mysql.connector as s
    x = s.connect(host='localhost',user='root',password='tiger',database='railways')
    y = x.cursor()
    x.autocommit = True
    a = int(input("USER_ID: "))
    b = input("PASS WORD: ")
    try:
        l = "select user_id from user where password='{}'".format(b)
        y.execute(l)
        data = list(y.fetchall()[0])
        if data[0] == a: 
            l = "select * from user where password='{}'".format(b)
            y.execute(l)
            data = list(y.fetchall()[0])
            print("USER_ID: ",data[0])
            print("FIRST NAME: ",data[1])
            print("LAST NAME: ",data[2])
            print("PHONE NO.: ",data[4])
            print("AGE: ",data[5])
            print("GENDER: ",data[6])
            print("DOB: ",data[7])
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

def seat_checking(h,f,g):
    import random
    x = random.randint(0,5)
    print("\nThere are",x,"trains available for the date",h,"from",f,"to",g)
    if x == 0:
        pass
    else:
        try:
            l =[]
            for i in range(1,x+1):
                w = random.randint(10000,99999)
                y = random.randint(00,23)
                z = random.randint(00,59)
                time = str(y)+":"+str(z)
                s = "Train "+str(w)+" at time "+str(time)
                l.append(s.split(" "))
                print(s)
            a = int(input("\nEnter the train number: "))
            for j in l:
                if a == int(j[1]):
                    time1 = j[4]
            print("For train",a,"following seats are available:")
            for i in range(4):
                b = random.randint(0,100)
                c = random.randint(0,100)
                e = random.randint(0,100)
                f = random.randint(0,100)
                d = {"GENERAL":b,"DISABLED":c,"WOMAN":e,"SLEEPER":f}
            for i in d:
                print(i,":",d[i])
            g = input("Choose the category: ").upper()
            if d[g] == 0:
                h == 0
                print("SORRY! ALL SEATS ARE RESERVED")
                return False
            else:
                h = random.randint(10,99)
                print("BOOKED SUCCESSFULLY!\n","Your assigned seat number is",h,"in",g,"category.")
                return True,a,time1,g,h
        except:
            print("Enter valid input.")
            return False

menu()
    




















