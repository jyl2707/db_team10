# -*- coding:utf-8 -*-

from datetime import datetime

from . import db


class BaseModel(object):
    pass


class Chart1(BaseModel, db.Model):

    __tablename__ = "twitter"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    timestamp_ms = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        resp_dict = {
            "created_at":
                self.created_at,
            "text":
                self.text,
            "id":
                self.id,
            "timestamp_ms":
                self.timestamp_ms,
        }
        return resp_dict

class User(BaseModel, db.Model):

    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    location = db.Column(db.String(32), nullable=True)
    url = db.Column(db.String(32), nullable=True)
    description = db.Column(db.String(32), nullable=True)
    protected = db.Column(db.String(32), nullable=True)
    verified = db.Column(db.String(32), nullable=True)
    created_at = db.Column(db.String(32), nullable=True)
    contributors_enabled = db.Column(db.String(32), nullable=True)
    follow_request_sent = db.Column(db.String(32), nullable=True)
    notifications = db.Column(db.String(32), nullable=True)

    # twitters = db.relationship('Chart1',
    #     uselist=True,
    #     backref='user', 
    #     lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            "name":
                self.name,
            "id":
                self.id,
            "location":
                self.location,
            "url":
                self.url,
            "description":
                self.description,
            "protected":
                self.protected,
            "verified":
                self.verified,
            "created_at":
                self.created_at,
            "contributors_enabled":
                self.contributors_enabled,
            "follow_request_sent":
                self.follow_request_sent,
            "notifications":
                self.notifications,
        }
        return resp_dict