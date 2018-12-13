# coding=utf-8

from sqlalchemy import create_engine
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yaml import load, dump
from pprint import pprint

with open('config_inc.yaml', 'r') as f:
    doc = load(f)

dbhost = doc['dbhost']
passowrd = doc['password']
user = doc['user']
database = doc['database']

pymysql.install_as_MySQLdb()
engine = create_engine("mysql://"+user+":"+passowrd+"@"+dbhost+"/"+database)
Session = sessionmaker(bind=engine)

Base = declarative_base()
