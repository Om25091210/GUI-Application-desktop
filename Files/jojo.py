import smtplib

sender_email="omyadav04352@gmail.com"
rec_email=input("enter receviers email")
password=input("enter your password")
message="HEY !,THIS WAS SENT USING PYTHON"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent to ",rec_email)

