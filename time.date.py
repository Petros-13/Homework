import calendar

for month in calendar.month_name:
    if month:  # Skip the empty string at index 0
        print(month)
