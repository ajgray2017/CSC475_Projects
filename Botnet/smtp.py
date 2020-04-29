class SMTP:
    def __init__(self, sender, receiver, password):
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.port = 465
        self.payloadName = ""
        self.subject = "S TEST"
        self.contents = "C TEST"

    def getPayload(self):
        # todo add in filename from server
        # return input("Enter FileName: ")
        return "email_body.txt"

    def sendEmail(self):
        import smtplib, ssl, pickle, mimetypes
        from email.message import EmailMessage

        message = EmailMessage()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject
        message.set_content(self.contents)

        aFile = self.getPayload()

        with open(aFile, "rb") as att:
            attachment = att.read()

        message.add_attachment(attachment, maintype="text", subtype="plain", filename=aFile)

        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls()
        session.login(self.sender, self.password)

        session.send_message(message, self.sender, self.receiver)
        session.quit()

        return True


if __name__ == "__main__":
    smtp = SMTP(sender, receiver, password)
    SMTP.__module__ = "smtp"
