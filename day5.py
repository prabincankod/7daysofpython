class Letterhead:
    sender = 'Nishchit Bhandari'
    def __init__(self,coordinator, id, subject, body):
        self.coordinator = coordinator
        self.id = id
        self.subject = subject
        self.body = body
    def compose_letter(self):
        letter = f'Letter number: {self.id}\nSubject: {self.subject}\n Dear {self.coordinator} sir, \n {self.body}\nYours,\n{Letterhead.sender}'
        return letter

class Email(Letterhead):
    def __init__(self, coordinator, id, subject, body, recipient):
        super().__init__(coordinator, id, subject, body)
        self.recipient = recipient
    def compose_email(self):
        email = f'Email number: {self.id}\nSubject: {self.subject}\n Dear {self.recipient}, \n {self.body}\nYours,\n{Letterhead.sender}'
        return email


newEmail=Email(body="this is a body.",coordinator="ramesh prashain",id="99",recipient="gagane@sallaghari.com",subject="regarding nothing.")
