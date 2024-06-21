from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer
from models.categories import Categories


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)

    category = relationship("Categories", foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Questions.category_id)

