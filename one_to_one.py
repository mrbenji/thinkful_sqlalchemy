#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport

session.add(beyonce)
session.commit()

print beyonce.passport.issue_date
print passport.owner.name