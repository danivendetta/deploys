# coding=utf-8

# 1 - imports
from datetime import date

from base import Session, engine, Base
from sitios import site
from deploy import deploy
from backup import backup
 
# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create site
site01 = site("tomcat-01", "PRO", "server01", "http://svn.server.local/trunk/", "/usr/local/tomcat/tomcat01/webapps", "0.0.0.0", "8080", "http://app01.server01.local")

#def __init__(self, aplicacion, entorno, ubicacion, svn_path, path, ip, puerto, url):

# 5 - create backup

#def __init__(self, site, path):

backup01 = backup("tomcat-01", "/var/backups/tomcat-01/")

# 6 - create deploy
#def __init__(self, site, entorno, backup_id):
deploy01 = deploy("tomcat-01", "PRO", backup01.backup_id)

# 6 - add data to deploy

deploy01.ejecutor = "Daniel"

# persist data
session.add(site01)
session.add(backup01)
session.add(deploy01)

# 10 - commit and close session
session.commit()
session.close()
