class SMTP:
    def __init__(self, sender, receiver, password, payloadName=None, subject=None, contents=None, port=587):
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.port = port
        self.payloadName = payloadName
        self.subject = subject
        self.contents = contents

    def main(self):
        import smtplib, ssl, pickle, mimetypes
        from email.message import EmailMessage

        message = EmailMessage()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject
        message.set_content(self.contents)
        
        if self.payloadName != None:
            try:
                with open(self.payloadName, "rb") as att:
                    attachment = att.read()
            except:
                print(self.payloadName)
                return False

        message.add_attachment(attachment, maintype="text", subtype="plain", filename=self.payloadName)

        session = smtplib.SMTP("smtp.gmail.com", self.port)
        session.starttls()
        session.login(self.sender, self.password)

        session.send_message(message, self.sender, self.receiver)
        session.quit()

        return True


if __name__ == "__main__":
    SMTP.__module__ = "smtp"
