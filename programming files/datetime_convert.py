// This code changes the format of the date from YYYY-MM-DD to MM/DD/YYYY
from datetime import datetime

date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

print(formatted_date)
