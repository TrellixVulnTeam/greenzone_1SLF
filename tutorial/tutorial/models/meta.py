from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

""" In a SQLAlchemy-based application, a 'model' object is an object composed
    by querying the SQL db. The 'models' package is where the alchemy 
    cookiecutter put the classes that implement my models. """

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: https://alembic.sqlalchemy.org/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

""" meta.py contains imports and support code for defining the models.
    it creates a dict 'NAMING_CONVENTION' as well for consistent
    naming of support objects like indices and constraints. """

metadata = MetaData(naming_convention=NAMING_CONVENTION)
""" Next create a metadata object from the class 
    'sqlalchemy.schema.MetaData', using 'NAMING_CONVENTION'
    as the value for the 'nameing_convention' argument.
    A 'MetaData' object represents the table and other
    schema definitions for a single db. """

Base = declarative_base(metadata=metadata)
""" Also create a declarative 'Base' object to use a
    base class for my other models. My models will inherit
    from this 'Base', which will attach the tabls to the 
    metadata created, and define my apps db schema. """
