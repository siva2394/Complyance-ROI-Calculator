# app/report.py
from fpdf import FPDF
from io import BytesIO

def generate_pdf_report(scenario_data: dict) -> BytesIO:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    # Title
    pdf.cell(0, 10, 'Invoicing Automation ROI Report', 0, 1, 'C')
    pdf.ln(10)

    # Scenario Name
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, f"Scenario: {scenario_data['scenario_name']}", 0, 1)
    pdf.ln(5)

    # --- Inputs Section ---
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Your Business Inputs", 0, 1)
    pdf.set_font("Arial", '', 10)
    inputs = scenario_data['inputs']
    pdf.cell(0, 7, f"  - Monthly Invoice Volume: {inputs['monthly_invoice_volume']}", 0, 1)
    pdf.cell(0, 7, f"  - AP Staff Count: {inputs['num_ap_staff']}", 0, 1)
    pdf.cell(0, 7, f"  - Average Hourly Wage: ${inputs['hourly_wage']:.2f}", 0, 1)
    pdf.cell(0, 7, f"  - Time Horizon: {inputs['time_horizon_months']} months", 0, 1)
    pdf.cell(0, 7, f"  - Implementation Cost: ${inputs['one_time_implementation_cost']:.2f}", 0, 1)
    pdf.ln(10)

    # --- Results Section ---
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Projected Savings & ROI", 0, 1)
    pdf.set_font("Arial", '', 10)
    results = scenario_data['results']
    pdf.cell(0, 8, f"  - Monthly Savings: ${results['monthly_savings']:,.2f}", 0, 1)
    pdf.cell(0, 8, f"  - Total Savings ({inputs['time_horizon_months']} months): ${results['cumulative_savings']:,.2f}", 0, 1)
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 8, f"  - Payback Period: {results['payback_months']:.1f} months", 0, 1)
    pdf.cell(0, 8, f"  - Return on Investment (ROI): {results['roi_percentage']:,.1f}%", 0, 1)
    pdf.ln(5)

    # Footer
    pdf.set_y(-25)
    pdf.set_font("Arial", 'I', 8)
    pdf.cell(0, 10, 'Thank you for using the Invoicing ROI Simulator!', 0, 0, 'C')

    # Return PDF as bytes
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer