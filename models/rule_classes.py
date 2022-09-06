#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : rule_classs.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/27

# from sqlalchemy import Column, String, Integer, Float, DateTime, Date, ForeignKey, Text
# from flask_sqlalchemy import SQLAlchemy
# d = SQLAlchemy()

def init(db):
    class RuleClass(db.Model):
        __tablename__ = 'rule_class'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(20),unique=True)
        class_name = db.Column(db.String(255))
        class_url = db.Column(db.String(255))
        cookie = db.Column(db.String(255))

        def __repr__(self):
            return "<RuleClass(name='%s', class_name='%s', class_url='%s',cookie='%s')>" % (
                self.name, self.class_name, self.class_url,self.cookie)

    # db.create_all()
    db.create_all()
    return RuleClass