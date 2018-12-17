# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
import datetime
from base import Base


class deploy(Base):
    __tablename__ = 'deploys'

    deploy_id = Column(Integer, primary_key=True)
    site = Column(String(250))
    entorno = Column(String(6))
    fecha = Column(Date, default=datetime.datetime.utcnow)
    ejecutor = Column(String(25))
    previous_version = Column(String(12))
    target_version = Column(String(12))
    backup_id = Column(Integer, ForeignKey('backups.backup_id'))
    backup = relationship("backup", backref=backref("deploys", uselist=False))
    is_urgente = Column(Boolean, default=False)


    def __init__(self, site, entorno, backup_id):

        self.site = site
        self.entorno = entorno
        self.backup_id = backup_id
