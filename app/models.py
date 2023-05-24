# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
    

class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    terminal_id = db.Column(db.Integer)
    port_id = db.Column(db.Integer)
    client_longitud = db.Column(db.Float)
    client_latitud = db.Column(db.Float)
    client_name = db.Column(db.String(200))
    client_vat = db.Column(db.String(13))
    client_address = db.Column(db.String(255))
