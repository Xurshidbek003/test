from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer
from models.answers import Answers
from models.categories import Categories
from models.questions import Questions
from models.users import Users


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)

    question = relationship("Questions", foreign_keys=[question_id],
                            primaryjoin=lambda: Questions.id == Results.question_id)

    answer = relationship("Answers", foreign_keys=[answer_id],
                          primaryjoin=lambda: Answers.id == Results.answer_id)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Results.user_id)

    category = relationship("Categories", foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Results.category_id)
