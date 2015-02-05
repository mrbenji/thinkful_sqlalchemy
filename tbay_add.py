#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://codio@localhost:5432/tbay")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from tbay import Item, User, Bid

user1 = User(username="Benji",password="benjipass")
user2 = User(username="Michael",password="michaelpass")
session.add_all([user1, user2])
session.commit()

item1 = Item(name="doodad", owner=user1)
item2 = Item(name="foodad", owner=user2)

session.add_all([item1, item2])
session.commit()

bid1 = Bid(price=100.0, bidder_id=user1, item_id=item2)
bid2 = Bid(price=200.0, bidder_id=user2, item_id=item1)

session.add_all([bid1, bid2])
session.commit()
