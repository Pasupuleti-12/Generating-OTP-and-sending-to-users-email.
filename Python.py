import random
import smtplib
username='psaibhavanivenkatesh@gmail.com'
password='fcgfllmvjyjzdjbp'
toaddress='pasupuleti1222002@gmail.com'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
otp=''.join([str(random.randint(0,9))for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
server.sendmail(username,toaddress,msg)
server.quit()                
