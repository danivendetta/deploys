# coding=utf-8

# 1 - imports
from datetime import date
from yaml import load, dump
from pprint import pprint
from base import Session, engine, Base
from sitios import site
from deploy import deploy
from backup import backup


with open('sites.yaml', 'r') as f:
    doc = load(f)

pprint(doc)

"""
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

"""
