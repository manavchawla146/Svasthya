from twilio.rest import Client as Call

from_number = "+13346103900"
to_number = "+919316183902"
src_path = "http://www.vothla.com/Twilio_Demo.xml"

client = Call("ACa536222f138dc72a96a015a1deb4cf43","e84f1d2aa41e9170d55099783ef82a85")

print("call initiated")
client.calls.create(to=to_number, from_=from_number, url = src_path, method = 'GET')
print('Call has been triggered successfully')


'''import smtplib
a=["manavchawla146@gmail.com"]

for i in range(1):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('scrap.id14@gmail.com', 'ikno nxfu lbii wgkn')

    ab="Name:  "
    io=input("")
    fh="Address= "
    oi=input("")
    y="Problem: Cardiac surgery"
    bsdk=y+"\n"+ab+"\n"+fh+oi+"\n"+y+"\n"+ab+io
    server.sendmail('scrap.id14@gmail.com', a[i],bsdk)
    print('Mail Sent')'''



