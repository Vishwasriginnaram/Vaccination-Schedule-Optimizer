from datetime import datetime, timedelta

def generate_reminders(schedule):
    reminders = []
    for item in schedule:
        try:
            vaccine_date = datetime.strptime(item["date"], '%Y-%m-%d')
            reminder_date = vaccine_date - timedelta(days=1)

            reminders.append({
                "reminder_date": reminder_date.strftime('%Y-%m-%d'),
                "message": f"Reminder: {item['vaccine']} scheduled for tomorrow ({vaccine_date.strftime('%Y-%m-%d')})"
            })
        except Exception as e:
            print("Reminder generation failed for entry:", item, "Error:", e)
            continue
    return reminders
