import pandas as pd

df = pd.read_csv('data/vaccination_schedule_dataset.csv')


def get_risk_level(region):
    region_df = df[df['Region'].str.lower() == region.lower()]
    if region_df.empty:
        return 0
    return round(region_df['Risk_Score'].mean(), 2)
