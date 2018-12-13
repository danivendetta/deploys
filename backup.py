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

    #def __init__(self, backup_id, site, fecha, path):
    def __init__(self, site, path):
        #self.backup_id = backup_id
        self.site = site
        #self.fecha = fecha
        self.path = path
