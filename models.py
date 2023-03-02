from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
import re

Base = declarative_base()


class EmailAddress(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Email({self.address})>"

    @validates("email")
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError("Invalid email adress")
        if key != "email":
            raise ValueError("Key must be 'email'")
        return address
