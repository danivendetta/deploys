# coding=utf-8

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date
import datetime
from base import Base


class backup(Base):
    __tablename__ = 'backups'

    backup_id = Column(Integer, primary_key=True)
    site = Column(String(250))
    fecha = Column(Date, default=datetime.datetime.utcnow)
    path = Column(String(250))


    def __init__(self, site, path):

        self.site = site
        self.path = path
