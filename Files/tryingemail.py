import smtplib

sender_email='omyadav04352@gmail.com'
sender_password='omyadavom'

def send_email(receiver_email,subject,body):
    message='Subject: {}\n\n{}'.format(subject,body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as server:
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,message)

if __name__=='__main__':
    send_email('amanrajyadav279@gmail.com','NOTIFICATION','Everything is Awesome!')
