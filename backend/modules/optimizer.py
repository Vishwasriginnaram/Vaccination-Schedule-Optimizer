from datetime import datetime, timedelta

def optimize_schedule(vaccines, risk_score, age, condition):
    schedule = []
    start_date = datetime.today()

    for i, vaccine in enumerate(vaccines):
        days_offset = i * 14  # 2-week gap
        vaccine_date = start_date + timedelta(days=days_offset)

        schedule.append({
            "day": days_offset,
            "date": vaccine_date.strftime('%Y-%m-%d'),
            "vaccine": vaccine,
            "reason": f"Recommended for age {age}, condition: {condition}, risk score: {risk_score}"
        })

    return schedule
