from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base

class MyModel(Base):
""" defined model class 'MyModel' """
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

    """ model does not require an __init__ method because SQLAlchemy
        supplies a default constructor, if one is not already present,
        which accepts keyword arguments of the same name as that of 
        the mapped attributes.

        Example use of MyModel:

        johnny = MyModel(name="John Doe", value=10) """

    """ MyModel class has a __tablename__ attribute. This informs SQLAlchemy
        which table to use to store the data representing instances of this class. """ 
  
Index('my_index', MyModel.name, unique=True, mysql_length=255)
