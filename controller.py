from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EmailAddress

class Controller:
    def __init__(self):
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)

    def save(self, email):
        email_address = EmailAddress(email)
        try:
            with Session(self.engine) as sess:
                sess.add(email_address)
                sess.commit()

            # show a success message
            return f'The email {email} saved! to database'

        except ValueError as error:
            # show an error message
            raise ValueError(error)
