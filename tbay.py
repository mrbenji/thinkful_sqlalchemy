#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
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
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids = relationship('Bid', backref='item')

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    bidder = relationship('Bid', backref='bidder')
    #auction_items = Column(Integer, ForeignKey('items.id', backref='items_for_sale'))
    item = relationship('Item', backref='owner')

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    price = Column(Float, nullable=False)
 
Base.metadata.create_all(engine)
