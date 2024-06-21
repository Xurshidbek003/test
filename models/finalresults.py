from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, Float
from models.users import Users


class FinalResults(Base):
    __tablename__ = 'final_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    common = Column(Integer, nullable=False)
    found = Column(Integer, nullable=False)
    percent = Column(Float, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == FinalResults.user_id)
