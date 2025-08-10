from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    company_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    hotline = Column(String, nullable=True)

    users = relationship("User", back_populates="company")
    documents = relationship("Document", back_populates="company")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String, CheckConstraint("role IN ('admin', 'user')"), nullable=False)
    company_id = Column(String, ForeignKey("companies.company_id"), nullable=False)

    company = relationship("Company", back_populates="users")
    feedback = relationship("Feedback", back_populates="user")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    company_id = Column(String, ForeignKey("companies.company_id"), nullable=False)
    file_name = Column(String, nullable=False)
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)

    company = relationship("Company", back_populates="documents")

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=True)
    rating = Column(Integer, CheckConstraint("rating BETWEEN 1 AND 5"))
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship("User", back_populates="feedback")
