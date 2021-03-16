import smtplib
content='hello....'
try:
     mail=smtplib.SMTP('smtp.gmail.com',587)
     mail.starttls()
     mail.login('iactmzn@gmail.com','password')
     mail.sendmail('iactmzn@gmail.com','iactmzn@gmail.com',content)
     print("Successfully sent email")
     mail.close()
except smtplib.SMTPException as e:
     print("error",e)
