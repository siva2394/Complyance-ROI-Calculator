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





-----

````markdown
# Invoicing ROI Simulator

This project is a lightweight ROI calculator designed to help businesses visualize the cost savings and payback period when switching from manual to automated invoicing systems. The application features a clean, single-page interface and a RESTful API backend built with Python and FastAPI.

This prototype was built as a 3-hour programming assignment, demonstrating full-stack capabilities with a focus on rapid delivery and meeting all specified requirements.

## ✨ Key Features

-   **Interactive Calculator:** A single-page web app with a form for user inputs and live, dynamically updated results.
-   **Instant ROI Analysis:** Calculates monthly savings, total savings, payback period, and ROI in real-time.
-   **Scenario Management:** Save and load different simulation scenarios by name, persisted in a local SQLite database.
-   **Email-Gated Reporting:** Generate a downloadable PDF summary of the ROI analysis, gated by an email input field to simulate lead capture.
-   **RESTful API:** A well-documented backend API to handle simulation logic and data persistence.

## 🛠️ Tech Stack

-   **Backend:** FastAPI, Uvicorn
-   **Database:** SQLite with SQLAlchemy ORM
-   **Frontend:** HTML, Vanilla JavaScript (Fetch API), Jinja2 for templating
-   **PDF Generation:** FPDF2
-   **Validation:** Pydantic

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8+
-   Git

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone [https://github.com/siva2394/Complyance-ROI-Calculator.git](https://github.com/siva2394/Complyance-ROI-Calculator.git)
cd Complyance-ROI-Calculator
````

### 2\. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3\. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

Once the setup is complete, you can run the web server using Uvicorn.

```bash
uvicorn app.main:app --reload
```

The application will be available at the following addresses:

  - **🌐 Frontend UI:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
  - **📄 API Docs (Swagger UI):** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

## ⚙️ API Endpoints

The application provides the following API endpoints. You can test them interactively via the [Swagger UI docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs).

| Method | Endpoint             | Purpose                               |
| :----- | :------------------- | :------------------------------------ |
| `POST` | `/simulate`          | Run simulation and return JSON results|
| `POST` | `/scenarios`         | Save a scenario to the database       |
| `GET`  | `/scenarios`         | List all saved scenarios             |
| `GET`  | `/scenarios/:id`     | Retrieve details for a single scenario|
| `POST` | `/report/generate`   | Generate a PDF report (email required)|

```
```
