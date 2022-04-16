import smtplib

def send_email(subject,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('omyadav04352@gmail.com','omyadavom')
        message="Subject {} {}".format(subject,msg)
        server.sendmail('omyadav04352@gmail.com','amanrajyadav249@gmail.com',message)
        server.quit()
        print("SUCCESS:EMAIL SENT")
    except:
        print("Email failed to send")
subject="TEST Subject"
msg="HELLO THERE,HOW ARE YOU TODAY?"
send_email(subject,msg)
