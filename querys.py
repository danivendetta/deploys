# coding=utf-8

# 1 - imports
from datetime import date

from base import Session, engine, Base
from sitios import site
from deploy import deploy
from backup import backup

# 2 - extract a session

session = Session()

# 3 - extract all movies
sites = session.query(site).all()

print('\n### All sites:')

for site in sites:
    print(f'{site.aplicacion} is in {site.ubicacion}')
print('')
