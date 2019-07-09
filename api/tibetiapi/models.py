from .db import Base
from .db import engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship("Project")


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    state = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String)
    attachments = relationship("Attachment")
    type = Column(String)
    __mapper_args__ = {"polymorphic_identity": "project", "polymorphic_on": type}


class Attachment(Base):
    __tablename__ = "attachment"
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    file_id = Column(Integer, ForeignKey("file.id"), primary_key=True)
    file = relationship("File")


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    url = Column(String)


class MultiClassMultiLabelClassificationEvaluateProject(Project):
    __tablename__ = "mcml_classification_evaluate_project"
    id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    training_data_file = Column(Integer)
    __mapper_args__ = {"polymorphic_identity": "mcml_classification_evaluate_project"}


def create_tables():
    Base.metadata.create_all(engine)
