import mysql.connector as imp
import smtplib

"""x=imp.connect(host='localhost', user='root',passwd='root',database="medi")
p=x.cursor()
name=input("Name: ")
aadh=int(input("Aadhar: "))
pol=input("Policy: ")
com=input("Company: ")
bud=int(input("Budget: "))
add=input("Address:")"""


a=["manavchawla146@gmail.com"]
for i in range(len(a)):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('scrap.id14@gmail.com', 'ikno nxfu lbii wgkn')
    
    ab="Name: Manav "
    
    fh="Address: Rohini Bunglows,Ahmedabad"
    y="Problem: Cardiac surgery"
    o="Aadhar: 123412341234"

    bsk=ab+"\n"+y+"\n"+ab+"\n"+fh
    
   

   
    server.sendmail('scrap.id14@gmail.com', a[i],bsk)

    print('Mail Sent')

"""print(ab+"\n",bc,"\n",cd,"\n",de,name,"\n",tt,str(aadh),"\n",pp,add,"\n",pc,"\n",ef,"\n",fg,"\n",gh)"""
       













    


