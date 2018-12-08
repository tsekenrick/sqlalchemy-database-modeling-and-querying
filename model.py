# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# declarative base 
from sqlalchemy.ext.declarative import declarative_base

# create the base class (declarative base)
# call it Base!
Base = declarative_base()


# implement the following three classes...
    

    
class ScooterType(Base):    
    __tablename__ = 'scooter_type'
    
    scooter_type_id = Column('scooter_type_id', Integer, primary_key=True)
    model = Column('model', String(50))
    max_range = Column('max_range', Integer)
    weight = Column('weight', Integer)
    max_speed = Column('max_speed', Integer)
    
    company_id = Column('company_id', Integer, ForeignKey('company.company_id'))
    manufacturer = relationship('Company', back_populates = 'scooter_types')
    
    # ???
    scooters = relationship('Scooter', back_populates = 'scooter_type')
    
    def __str__(self):
        return f'Company Name: {self.manufacturer.name}\nModel {self.model}\nMax Speed {self.max_speed}\nWeight {self.weight}'
        # return f'{self.manufacturer} {self.model}: max speed is {self.max_speed}'
    def __repr__(self):
        return self.__str__()

    
class Company(Base):
    __tablename__ = 'company'
    
    company_id = Column('company_id', Integer, primary_key=True)
    name = Column('name', String(50))
    website = Column('website', String(50))
    founded = Column('founded', Integer)
    
    scooter_types = relationship(ScooterType, back_populates='manufacturer')

    def __str__(self):
        return f'{self.name} - Website: {self.website} - Est. {self.founded}'
    
    def __repr__(self):
        return self.__str__()

class Scooter(Base):
    __tablename__ = 'scooter'

    scooter_id = Column('scooter_id', Integer, primary_key=True)    
    acquired_date = Column('acquired_date', Date)
    retired = Column('retired', Boolean, default=False)
    
    # one-to-many for scooter type to scooters
    scooter_type_id = Column('scooter_type_id', Integer, ForeignKey('scooter_type.scooter_type_id'))
    scooter_type = relationship('ScooterType', back_populates = 'scooters')
    
    def __str__(self):
        return f'Scooter #{self.scooter_id}\nRetired? {self.retired}\nScooter Type:\n{self.scooter_type}'

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        data = {
                'acquired_date': self.acquired_date.strftime('%Y-%m-%d'),
                'retired': self.retired,
                'scooter_type': self.scooter_type.model,
                'max_speed': self.scooter_type.max_speed,
                'weight': self.scooter_type.weight,
                'manufacturer': self.scooter_type.manufacturer.name,
                'website': self.scooter_type.manufacturer.website
                }
        
        return data