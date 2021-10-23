# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:46:29 2020

@author: komal
"""
import pandas as pd
import mysql.connector as c
db=c.connect(host='localhost',database='schoolmanagement',user='divesh',passwd='8318')
if db.is_connected():
    print("connection is successfully done")
    
def menu():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     SCHOOL MANAGEMENT SYSTEM (PROJECT)                   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("MENU    ")
    print("     STUDENT_DETAILS")
    print("     1. About")
    print("     2. Show Tables")
    print("     3. Describe Table student_details")
    print("     4. Show All Records from student_details")
    print("     5. Add student_details")
    print("     6. Delete from student_details")
    print("     7. Update student_details from Table")
    print()
    print("     MARKS")
    print("     8. Describe Table marks")
    print("     9. Show All Records from marks")
    print("    10. Add Detail in marks table")
    print("    11. Delete from marks table")
    print("    12. Update Marks table")
    print("    13. Search marks by admission no")
    print()
    print("     Fees_Details")
    print("    14. Describe Table Fees Details")
    print("    15. Show All Records from fee_details")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
menu()
def about():
    print("In This School Management System Project there are 3 tables and 15 options")

def show_tables():
    print("Show names of tables in the database of schoolmanagament")
    mc=db.cursor()
    mc.execute("Show tables;")
    for x in mc:
        print(x)
        
def desc_student_details():
    print('show structure of student_detail table')
    df=pd.read_sql("desc student_details;",db)
    print(df)
    
def show_recordsstudent_details():
    print('All records of student_detail')
    df=pd.read_sql("select * from student_details;",db)
    print(df)
    
def add_student_details():
    print('Before any changes in table')
    df=pd.read_sql("select * from student_details;",db)
    print(df)
    print('insert into student_details new admission')
    mc=db.cursor()
    sql="insert into student_details(Admission_No,Student_Name,Class_Section,Father_Name,Phone_No,Address)"
    val=('106XX','Rahul','12-C2','Ansh','813347','Lalbagh')
    mc.execute(sql,val)
    print("Done")
    db.commit()
    df=pd.read_sql("select * from student_details;",db)
    print(df)
    print("record inserted in our table")
    
def del_student_details():
     print('Before any changes in table')
     df=pd.read_sql("select * from student_details;",db)
     print(df)
     print()
     mc=db.cursor()
     mc.execute("Delete from student_detail where Admission_No='105XX';")
     print("Record Deleted")
     db.commit()
     
def update_student_detail():
    print('Before any changes in table')
    df=pd.read_sql("select * from student_details;",db)
    print(df)
    print()
    mc=db.cursor
    mc.execute("Update Student_Deatil set address=Charbagh where Admission_No='105XX'")
    print("Record Updated")
    db.commit()
    df.pd.read_sql("select * from student_details;",db)
    print(df)
    
def desc_marks():
    print('show structure of marks table')
    df=pd.read_sql("desc marks;",db)
    print(df)

def show_records_marks():
    print('All records of marks')
    df=pd.read_sql("select * from marks;",db)
    print(df)
    
def add_marks():
    print('Before Any Changes')
    df=pd.read_sql("select * from marks;",db)
    print(df)
    print('insert into marks new test marks')
    mc=db.cursor()
    sql="insert into marks(Admission_No varchar(10),Student_Name char(15),Class_Section varchar(9),Phone_No int,Out_Of_Marks int,Economics int,Accountancy int,Business_Studies int,Computer_Science int,English int,Total_Marks int)"
    val=('106XX',"Rahul",'12-C2','813347',500,'71',75,'90','81',70,'387')
    mc.execute(sql,val)
    print("Done")
    db.commit()
    df=pd.read_sql("select * from marks;",db)
    print(df)
    print("Record Inserted")
    
def del_marks():
     print('Before any changes in table')
     df=pd.read_sql("select * from marks;",db)
     print(df)
     print()
     mc=db.cursor()
     mc.execute("Delete from marks where Admission_No='106XX'")
     print("Record Deleted")
     db.commit()
     
def update_marks():
    print('Before any changes in table')
    df=pd.read_sql("select * from student_details;",db)
    print(df)
    print()
    mc=db.cursor
    mc.execute("Update Student_Deatil set Phone_No=997665 where Admission_No='105XX'")
    print("Record Updated")
    db.commit()
    df.pd.read_sql("select * from student_details;",db)
    print(df)

def search_by_admissiono():
    print("Search Student Record by entering Roll no.")
    a=int(input("Enter Roll Number:"))
    qry="select * from marks where Admission_No=%s;"%(a,)
    df=pd.read_sql(qry,db)
    print(df)
    
def desc_fees_details():
    print('show structure of fees_details table')
    df=pd.read_sql("desc fee_details;",db)
    print(df)

def show_records_fees_details():
    print('All records of fee_details')
    df=pd.read_sql("select * from fee_detail;",db)
    print(df)

#main

opt=""
opt=int(input("Enter your choice"))
if opt==1:
    about()
elif opt==2:
    show_tables()
elif opt==3:
    desc_student_details()
elif opt==4:
    show_recordsstudent_details()
elif opt==5:
    add_student_details()
elif opt==6:
    del_student_details()
elif opt==7:
    update_student_detail()
elif opt==8:
    desc_marks()
elif opt==9:
    show_records_marks()
elif opt==10:
    add_marks()
elif opt==11:
    del_marks()
elif opt==12:
    update_marks()
elif opt==13:
    search_by_admissiono()
elif opt==14:
    desc_fees_details()
elif opt==15:
    show_records_fees_details()

else:
    print("Invalid Option")
    
import winsound
winsound.Beep(1000,300)