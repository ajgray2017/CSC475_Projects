import smtplib, ssl

# choosing the smtp port
port = 465 
pswrd = input("Gmail Password: ")

# Create SSL context
context = ssl.create_default_context()

# sending a message directly from python (no txt file)
sender_email = "hellotest001smtp@gmail.com"
receiver_email = "hellotest001smtp@gmail.com"
message = """\
    Subject: Hi There

    This message was sent to you via Python."""

# makes sure that the connection is severed when complete
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("hellotest001smtp@gmail.com", pswrd)
    server.sendmail(sender_email, receiver_email, message)
