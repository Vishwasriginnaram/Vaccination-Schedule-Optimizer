from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from modules.reminder import generate_reminders

from modules.eligibility import check_eligibility
from modules.risk_analyzer import get_risk_level
from modules.optimizer import optimize_schedule

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app) 

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    data = request.json
    age = int(data['age'])
    condition = data.get('condition', 'none')
    region = data['region']

    vaccines = check_eligibility(age, condition)
    risk_score = get_risk_level(region)
    schedule = optimize_schedule(vaccines, risk_score, age, condition)
    reminders = generate_reminders(schedule)

    return jsonify({
        "schedule": schedule,
        "reminders": reminders
    })

if __name__ == '__main__':
    app.run(debug=True)
