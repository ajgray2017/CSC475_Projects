import smtplib, ssl
import getpass

# choosing the smtp port
port = 465 
pswrd = getpass.getpass()       # getpass function that will get the password w/o showing it
dummy_file = input("What file did you want to generate an email from? ")

# Create SSL context
context = ssl.create_default_context()

# sending a message directly from python (no txt file)
sender_email = "hellotest002smtp@gmail.com"
receiver_email = "hellotest001smtp@gmail.com"
message = " "

# opens up the txt file and fills the message variable with info from the file
with open(dummy_file) as line:
    for x in line:
        message += x

print(message)      # check that the message is being pulled from the dummy txt file

# makes sure that the connection is severed when complete
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, pswrd)
    print("Sending messages")
    server.sendmail(sender_email, receiver_email, message)
