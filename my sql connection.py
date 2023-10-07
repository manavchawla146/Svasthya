'''import mysql.connector as m
mydb=m.connect(host='localhost',user='root',passwd="root")
mycursor=mydb.cursor()                                      # to connect and create database in mysql
mycursor.execute("CREATE DATABASE champ")
print(mydb)
import mysql.connector as e
abc=e.connect(host="localhost",user="root",passwd="root",database='satellite')
curr=abc.cursor()                                           # to show databases present in mysql
curr.execute("update from sat values ")
print("done")
for x in curr:
    print(x)
import mysql.connector as m
mydb=m.connect(host='localhost',user='root',passwd='root',database='satellite')
x=mydb.cursor()
x.execute("create table chomu(Name varchar(30),class int,Expected_marks int)")
mydb.commit()
print("Done")'''

import mysql.connector as m
mydb=m.connect(host='localhost',user='root',passwd='root',database='satellite')
x=mydb.cursor()                                 # show data from sat
x.execute("Select * from sat where Region='INDIA'")
#x.execute("Select * from sat")
y=x.fetchone()
print(y)

print("done")




'''import mysql.connector as m
mydb=m.connect(host='localhost',user='root',passwd='root',database='satellite')
x=mydb.cursor()                                                                                                                          #show data from sat
x.execute("Select S_name from sat where Region='INDIA' and Launch_Date ='May 19 2022 '")
print(x)




lst=[]
stack=[0,1,2,3,4,5,6,7,8,9,10]
def op():
    for i in stack:
        
        if i%2!=0:
            lst.append(i)
    print(lst)
op()
'''
