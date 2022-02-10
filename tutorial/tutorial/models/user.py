import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


"""
Basic model for a user who can authenticate to the wiki

The User class will  have class-level attributes named
'id, name, password_hash and role' all instances of 
sqlalchemy.schema.Column . These map to columns in the 
'users' table. The 'id' attribute will be the primary key
in the table. 'name' will be a unique string text attrbute 
in a text column. 'password_hash' will be a nullable text 
attribue that will contain a securely hashed password.
'role' is a text attribute that will hold the role of the user.

"""

class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    role = Column(Text, nullable=False)

    password_hash = Column(Text)

    def set_password(self, pw):
        pwhash = bcrypt.haspw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expect_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
