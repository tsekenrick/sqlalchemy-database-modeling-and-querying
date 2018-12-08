from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
from datetime import datetime
import random

Session = sessionmaker(db.engine)
session = Session()

# use the session object and imported classes (Company, Scooter, etc.)
# ... to create companies, types and scooters in teh database

################### Companies

companies = []

c1 = Company()
c1.name = 'Fast Company'
c1.website = 'fastco.com'
c1.founded = 2000
companies.append(c1)

c2 = Company()
c2.name = 'Generic Company'
c2.website = 'genco.com'
c2.founded = 2008
companies.append(c2)

c3 = Company()
c3.name = 'Special Company'
c3.website = 'vspecial.com'
c3.founded = 2014
companies.append(c3)

################### Scooter Types

scooter_types = []

st1 = ScooterType()
st1.model = 'FC Mk.1'
st1.max_range = 300
st1.weight = 30
st1.max_speed = 50
st1.manufacturer = c1 
scooter_types.append(st1)

st2 = ScooterType()
st2.model = 'FC Lite'
st2.max_range = 400
st2.weight = 20
st2.max_speed = 40 
st2.manufacturer = c1
scooter_types.append(st2)

st3 = ScooterType()
st3.model = 'FC Pro'
st3.max_range = 500
st3.weight = 50
st3.max_speed = 70 
st3.manufacturer = c1
scooter_types.append(st3)

###################

st4 = ScooterType()
st4.model = 'GC Generic'
st4.max_range = 200
st4.weight = 35
st4.max_speed = 60 
st4.manufacturer = c2
scooter_types.append(st4)

st5 = ScooterType()
st5.model = 'GC Boring'
st5.max_range = 250
st5.weight = 40
st5.max_speed = 55 
st5.manufacturer = c2
scooter_types.append(st5)

st6 = ScooterType()
st6.model = 'GC Coma Inducing'
st6.max_range = 150
st6.weight = 30
st6.max_speed = 20 
st6.manufacturer = c2
scooter_types.append(st6)

###################

st7 = ScooterType()
st7.model = 'SC Sonic'
st7.max_range = 100
st7.weight = 15
st7.max_speed = 90
st7.manufacturer = c3
scooter_types.append(st7)

st8 = ScooterType()
st8.model = 'SC Juggernaut'
st8.max_range = 600
st8.weight = 100
st8.max_speed = 50
st8.manufacturer = c3
scooter_types.append(st8)

################### Scooters
# set type, retired and acquire date
scooters = []
retired = [True, False, False, False] # creates roughly .25 chance retired

for i in range(80):
    tmp_scooter = Scooter()
    
    tmp_scooter.scooter_type = random.choice(scooter_types)
    tmp_scooter.acquired_date = f'{random.randint(2014,2018)}-{random.randint(1, 12):02}-{random.randint(1,28):02}'
    tmp_scooter.retired = random.choice(retired)
    
    scooters.append(tmp_scooter)
    
session.add_all(scooters)
session.commit()
    
    

# assuming session is created and all imports are present:
companies = session.query(Company)
for c in companies:
    print(f'The company, {c}, has the following scooter models:');
    for i, scooter_type in enumerate(c.scooter_types):
        print(i + 1, scooter_type)
    print('\n')
 
scooter_types = session.query(ScooterType)
for s in scooter_types:
    print(f'{s.manufacturer.name} ==> {s.model}')
 
 