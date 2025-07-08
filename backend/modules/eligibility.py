import pandas as pd
import os
df = pd.read_csv('data/vaccination_schedule_dataset.csv')


def convert_age_group(age):
    if age < 1:
        return 'Infant'
    elif age < 5:
        return 'Toddler'
    elif age < 13:
        return 'Child'
    elif age < 20:
        return 'Teen'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

def check_eligibility(age, condition):
    age_group = convert_age_group(age)
    matched = df[(df['Age_Group'] == age_group) & 
                 ((df['Health_Condition'] == condition) | (df['Health_Condition'] == 'none'))]
    return matched['Vaccine'].unique().tolist()
