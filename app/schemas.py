# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any

# --- Input Schemas ---
class SimulationInput(BaseModel):
    monthly_invoice_volume: int
    num_ap_staff: int
    avg_hours_per_invoice: float
    hourly_wage: float
    error_rate_manual: float
    error_cost: float
    time_horizon_months: int
    one_time_implementation_cost: Optional[float] = 0.0

class ScenarioCreate(BaseModel):
    scenario_name: str
    inputs: SimulationInput

class ReportRequest(BaseModel):
    email: EmailStr
    scenario_id: int

# --- Output/Response Schemas ---
class SimulationResult(BaseModel):
    monthly_savings: float
    cumulative_savings: float
    net_savings: float
    payback_months: float
    roi_percentage: float

class Scenario(BaseModel):
    id: int
    scenario_name: str
    inputs: Dict[str, Any]
    results: Dict[str, Any]

    class Config:
        from_attributes = True # Changed from orm_mode for Pydantic v2

class ScenarioInfo(BaseModel):
    id: int
    scenario_name: str