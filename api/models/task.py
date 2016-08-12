from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.orm import relationship

from . import base
Base = base.Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    remark = Column(String(512))
    deadline = Column(Date, nullable=False)
    done = Column(Boolean, default=False)

    def __repr__(self):
        return "<Task (name='%s', remark='%s')>" % (self.name, self.remark)    
