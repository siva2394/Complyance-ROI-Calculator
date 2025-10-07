# Invoicing ROI Simulator

This is a lightweight ROI calculator that helps users visualize cost savings and payback when switching from manual to automated invoicing. This prototype was built in under 3 hours as per the PRD specification.

## Tech Stack

- **Backend**: FastAPI
- **Database**: SQLite (via SQLAlchemy ORM)
- **Frontend**: Single-Page App using HTML, vanilla JavaScript, and Jinja2 for templating.
- **PDF Generation**: FPDF2

## ⚙️ Setup and Installation

Follow these steps to get the application running locally.

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd roi_simulator
```
## 2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
## 3. Install Dependencies
Install all the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
🚀 Running the Application
Once the setup is complete, you can run the web server using Uvicorn.

Bash

uvicorn app.main:app --reload
The --reload flag enables hot-reloading, so the server will restart automatically when you make changes to the code.

The application will be available at:

Frontend UI: http://127.0.0.1:8000

API Docs (Swagger UI): http://127.0.0.1:8000/docs

# ✅ How to Use and Test
Quick Simulation:

Open your browser to http://127.0.0.1:8000.

The calculator will load with default values.

Change any input field, and the results on the right will update instantly upon clicking the "Calculate ROI" button.

Scenario Management:

Save: After getting a result you like, enter a name in the "Scenario Name" field and click "Save Scenario". A confirmation will appear.

Load: The "Saved Scenarios" dropdown will now contain your saved scenario. Select it from the list to load its inputs and results back into the calculator.

Report Generation:

To download a report, you must first save the scenario.

Once a scenario is saved and loaded, the "Download Full Report (PDF)" button will be active.

Click the button. A modal will appear asking for your email address.

Enter a valid email and click "Download Now". A PDF report summarizing the inputs and results will be downloaded by your browser.

# API Testing:

Navigate to http://127.0.0.1:8000/docs.

You can use the interactive Swagger UI to test all API endpoints (/simulate, /scenarios, /report/generate, etc.) directly.

🗃️ Database
The application uses a local SQLite database file named roi_simulator.db, which will be automatically created in the root directory (/roi_simulator) the first time you run the application. It stores all the saved scenarios.