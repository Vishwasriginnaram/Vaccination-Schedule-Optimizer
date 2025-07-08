# Vaccination Schedule Optimizer

An intelligent web-based system that generates personalized vaccination schedules based on age, health conditions, and regional disease outbreaks. It also provides automated reminder alerts for upcoming vaccinations.

---

## Features

- Personalized vaccine recommendations based on age & health status
- Region-based outbreak risk analysis using real dataset
- Smart scheduling with 2-week spacing logic
- Reminder alerts 1 day before each scheduled vaccine
- Interactive and beautiful frontend with cards, dropdowns, and loaders
- Modular Flask backend with separate components for eligibility, optimization, risk analysis, and reminders

---

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, Flask-CORS
- Data Handling: Pandas
- Dataset: vaccination_schedule_dataset.csv


---

## Setup Instructions

### 1. Clone and Navigate
bash
git clone https://github.com/yourusername/Vaccination-Schedule-Optimizer.git
cd Vaccination-Schedule-Optimizer/backend


### 2. Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux


### 3. Install Dependencies
bash
pip install flask pandas flask-cors


### 4. Run Backend Server
bash
python app.py


### 5. Open Frontend
Use Live Server extension in VS Code or open frontend/index.html directly in a browser.

---

## Sample Output


2025-07-08 (Day 0): Influenza
Reason: Recommended for age 20, condition: diabetes, risk score: 4.15

2025-07-22 (Day 14): COVID-19
Reason: Recommended for age 20, condition: diabetes, risk score: 4.15


### Reminder Alerts

2025-07-07: Reminder: Influenza scheduled for tomorrow (2025-07-08)
2025-07-21: Reminder: COVID-19 scheduled for tomorrow (2025-07-22)


---
