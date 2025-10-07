# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
import json

def get_scenario(db: Session, scenario_id: int):
    return db.query(models.Scenario).filter(models.Scenario.id == scenario_id).first()

def get_scenarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Scenario).offset(skip).limit(limit).all()

def create_scenario(db: Session, name: str, inputs: dict, results: dict):
    db_scenario = models.Scenario(
        scenario_name=name,
        inputs=inputs,
        results=results
    )
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario