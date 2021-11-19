from datetime import date, time, datetime, timedelta
today = date.today()
guaiguaibith = date(today.year, 3, 23)
if today > guaiguaibith:
    next_year = today.year + 1
    guaiguaibith = date(next_year, 3, 23)
days_until = (guaiguaibith - today).days
print(f"{days_until} day(s) Guaiguai's birthday.")
