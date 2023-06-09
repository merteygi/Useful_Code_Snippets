# This updated code takes into account the specific weekday (e.g., third Thursday) for each date. 
# It finds the first day of the same month in the previous year, calculates the number of days needed to reach the target weekday, 
# and retrieves the comparable date from the previous year accordingly.


import pandas as pd
from datetime import datetime, timedelta

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)

# Create a range of dates from January 1, 2022, to yesterday
date_range = pd.date_range(start='2022-01-01', end=yesterday, freq='D')

# Create a DataFrame using the date range
df = pd.DataFrame({'date': date_range})

# Sort the DataFrame by date in descending order
df.sort_values('date', ascending=False, inplace=True)

# Create a lambda function to calculate the comparable date
get_comparable_date = lambda date: datetime(date.year - 1, date.month, 1) + timedelta(
    days=((date.weekday() - datetime(date.year - 1, date.month, 1).weekday()) % 7) + ((date.isocalendar()[1] - 1) * 7)
)

# Apply the lambda function to the 'date' column and assign the result to a new column 'comparable_date'
df['comparable_date'] = df['date'].apply(get_comparable_date)

# Print the DataFrame
df
