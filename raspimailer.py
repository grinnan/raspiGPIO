import smtplib

fromaddr = 'from@gmail.com'
toaddrs  = ['email1@email.com','email2@email.com']
msg = '''\
From: from@gmail.com
Subject: This is a test for our notification system TEST2'

There was a terrible error that occured and I wanted you to know!'''

# Credentials (if needed)
username = 'username'
password = 'password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

