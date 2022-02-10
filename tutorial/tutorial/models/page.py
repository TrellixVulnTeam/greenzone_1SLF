from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from .meta import Base

"""
'creator_id' references the users table. Relating user objects
with page objects. Also define a 'creator' attribute as an
ORM-level mapping between the two tables. SQLAlchemy will
automatically populate this value useng the ForeignKey 
reference to the user. Since foreign key has 'nullable=False'
it is guaranteed that an instance of 'page' will have a 
corrosponding 'page.creator', which will be a 'User' instance.
"""

class Page(Base):
    """ The SQLAlchemy delcarative model class for a Page object. """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    data = Column(Text, nullable=False)

    creator_id = Column(ForeignKey('users.id'), nullable=False)
    creator = relationship('User', backref='created_pages')
