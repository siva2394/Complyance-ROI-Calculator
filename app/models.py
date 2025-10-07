# app/models.py
from sqlalchemy import Column, Integer, String, Float, JSON
from .database import Base

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    scenario_name = Column(String, index=True, unique=True)
    
    # User Inputs
    inputs = Column(JSON)
    
    # Calculated Results
    results = Column(JSON)