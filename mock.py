from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
from datetime import datetime
import random

Session = sessionmaker(db.engine)
session = Session()

# use the session object and imported classes (Company, Scooter, etc.)
# ... to create companies, types and scooters in teh database
