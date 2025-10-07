# app/main.py
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas, report
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# --- Internal Constants (Server-Side Only) ---
AUTOMATED_COST_PER_INVOICE = 0.20
ERROR_RATE_AUTO = 0.001  # 0.1%
TIME_SAVED_PER_INVOICE_MINUTES = 8 # This is not directly used in formula, but is an assumption
MIN_ROI_BOOST_FACTOR = 1.1

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Calculation Logic ---
def run_simulation_logic(inputs: schemas.SimulationInput) -> schemas.SimulationResult:
    # 1. Manual labor cost per month
    # Note: PRD formula was slightly ambiguous. A better interpretation is:
    # Total hours = num_staff * avg_hours_worked_by_staff. We will stick to the provided one.
    labor_cost_manual = (
        inputs.monthly_invoice_volume * inputs.avg_hours_per_invoice * inputs.hourly_wage
    )
    
    # 2. Automation cost per month
    auto_cost = inputs.monthly_invoice_volume * AUTOMATED_COST_PER_INVOICE
    
    # 3. Error savings
    manual_error_rate_decimal = inputs.error_rate_manual / 100
    error_savings = (
        (manual_error_rate_decimal - ERROR_RATE_AUTO) *
        inputs.monthly_invoice_volume *
        inputs.error_cost
    )
    
    # 4. Monthly savings (pre-bias)
    monthly_savings_pre_bias = (labor_cost_manual + error_savings) - auto_cost

    # 5. Apply bias factor
    monthly_savings = monthly_savings_pre_bias * MIN_ROI_BOOST_FACTOR
    
    # 6. Cumulative & ROI
    cumulative_savings = monthly_savings * inputs.time_horizon_months
    net_savings = cumulative_savings - inputs.one_time_implementation_cost
    
    if inputs.one_time_implementation_cost > 0 and monthly_savings > 0:
        payback_months = inputs.one_time_implementation_cost / monthly_savings
        roi_percentage = (net_savings / inputs.one_time_implementation_cost) * 100
    else:
        payback_months = 0.0
        roi_percentage = float('inf') # Effectively infinite ROI if no cost

    return schemas.SimulationResult(
        monthly_savings=round(monthly_savings, 2),
        cumulative_savings=round(cumulative_savings, 2),
        net_savings=round(net_savings, 2),
        payback_months=round(payback_months, 1),
        roi_percentage=round(roi_percentage, 1)
    )

# --- API Endpoints ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/simulate", response_model=schemas.SimulationResult)
def simulate_roi(inputs: schemas.SimulationInput):
    """Run simulation and return JSON results."""
    results = run_simulation_logic(inputs)
    return results

@app.post("/scenarios", response_model=schemas.Scenario, status_code=201)
def create_new_scenario(scenario: schemas.ScenarioCreate, db: Session = Depends(get_db)):
    """Save a scenario."""
    results = run_simulation_logic(scenario.inputs)
    db_scenario = crud.create_scenario(
        db=db,
        name=scenario.scenario_name,
        inputs=scenario.inputs.dict(),
        results=results.dict()
    )
    return db_scenario

@app.get("/scenarios", response_model=List[schemas.ScenarioInfo])
def list_all_scenarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all scenarios."""
    scenarios = crud.get_scenarios(db, skip=skip, limit=limit)
    return scenarios

@app.get("/scenarios/{scenario_id}", response_model=schemas.Scenario)
def get_scenario_details(scenario_id: int, db: Session = Depends(get_db)):
    """Retrieve scenario details."""
    db_scenario = crud.get_scenario(db, scenario_id=scenario_id)
    if db_scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return db_scenario

@app.post("/report/generate")
async def generate_report(req: schemas.ReportRequest, db: Session = Depends(get_db)):
    """Generate a PDF report (email required)."""
    scenario = crud.get_scenario(db, scenario_id=req.scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

    # The email is "captured" here. In a real app, you'd save it.
    print(f"Lead captured: {req.email} requested report for scenario {scenario.scenario_name}")

    scenario_data = {
        "scenario_name": scenario.scenario_name,
        "inputs": scenario.inputs,
        "results": scenario.results,
    }
    
    pdf_buffer = report.generate_pdf_report(scenario_data)

    headers = {
        'Content-Disposition': f'attachment; filename="ROI_Report_{scenario.scenario_name}.pdf"'
    }
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers=headers)