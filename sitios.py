#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, Date

from base import Base

class site(Base):

    __tablename__ = 'site'

    aplicacion = Column(String(250), primary_key=True)
    alias = Column(String(60))
    entorno = Column(String(6))
    ubicacion = Column(String(250))
    svn_url = Column(String(250))
    path = Column(String(250))
    ip = Column(String(250))
    puerto = Column(Integer)
    url = Column(String(250))
    last_deploy = Column(Integer)
    last_rollback = Column(Integer)

    def __init__(self, aplicacion, entorno, ubicacion, svn_url, path, ip, puerto, url):
        self.aplicacion = aplicacion
        self.entorno = entorno
        self.ubicacion = ubicacion
        self.svn_url = svn_url
        self.path = path
        self.ip = ip
        self.puerto = puerto
        self.url = url
