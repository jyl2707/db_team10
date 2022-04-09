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

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    profile_image_ur = db.Column(db.String(32), nullable=False)
    # twitters = db.relationship('Chart1',
    #     uselist=True,
    #     backref='user', 
    #     lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            "name":
                self.name,
            "profile_image_ur":
                self.profile_image_ur,
            "id":
                self.id,
        }
        return resp_dict