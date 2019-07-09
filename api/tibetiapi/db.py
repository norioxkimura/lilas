import sqlalchemy
import sqlalchemy.ext.declarative


Base = sqlalchemy.ext.declarative.declarative_base()
engine = sqlalchemy.create_engine("sqlite:///db.sqlite")
