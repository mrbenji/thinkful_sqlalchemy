#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Float, DateTime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://codio@localhost:5432/tbay")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

# class names should always be singular
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    seller = relationship("User", backref='items')
    bids = Column(Integer, ForeignKey(bids.id, backref='items'))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auction_items = Column(Integer, ForeignKey(items.id, backref='users'))

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
 
Base.metadata.create_all(engine)
