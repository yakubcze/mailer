import os
from datetime import timedelta, date, datetime
import calendar
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv # For .env files storing secrets

import mailer #mailer.py

load_dotenv(find_dotenv()) # Load the .env file.

directory = os.path.dirname(os.path.abspath(__file__))
today = datetime.today()
this_year = today.year
this_month = today.month

hourly_pay = int(os.getenv("HOURLY_PAY"))

# Scopes needed for the API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_KEY_FILE = 'service_account_key.json'

def main():
    # Login to Google using Service Account (using pickle was not ideal due to login expiration - unable to launch in LXC)
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
    
    if (this_month == 1): # If it is January of new year, get events for December of last year
        events_list = getEvents(service, 12, this_year-1)
        table_to_send = createTable(12, this_year-1, events_list)
        subject = f"Výplatní páska {12}/{this_year-1}"
    else: # Else get events for previous month
        events_list = getEvents(service, this_month-1, this_year)
        table_to_send = createTable(this_month-1, this_year, events_list)
        subject = f"Výplatní páska {this_month-1}/{this_year}"

    mailer.sendEmail(table_to_send, str(subject))

def getEvents(service, month, year):
    # Call the Calendar API
    date_begin = datetime(year, month, 1).isoformat() + 'Z'
    date_end = datetime(year, month, calendar.monthrange(year, month)[1]).isoformat() + 'Z'
    
    events_result = service.events().list(calendarId=os.getenv("CALENDAR_ID"), 
                                          timeMin=date_begin,
                                          timeMax=date_end,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    events_list = []

    if not events:
        return(["Žádné události nebyly získány!"])
    
    for event in events:
        if(event['summary'] == "Práce"):
            start = (event['start'].get('dateTime', event['start'].get('date'))).split('+')
            start_dt = datetime.strptime(start[0], "%Y-%m-%dT%H:%M:%S")

            end = (event['end'].get('dateTime', event['end'].get('date'))).split('+')
            end_dt = datetime.strptime(end[0], "%Y-%m-%dT%H:%M:%S")
            
            events_list.append([start_dt, end_dt])

    return(events_list)

def dateRangeList(start_date, end_date):
    # Return list of datetime.date objects (inclusive) between start_date and end_date (inclusive).
    date_list = []
    curr_date = start_date
    while curr_date <= end_date:
        date_list.append(curr_date)
        curr_date += timedelta(days=1)
    return date_list

def weekdayTranslate(weekday):
    if(weekday == 0):
        return("Ponděli")
    elif(weekday == 1):
        return("Úterý")
    elif(weekday == 2):
        return("Středa")
    elif(weekday == 3):
        return("Čtvrtek")
    elif(weekday == 4):
        return("Pátek")
    elif(weekday == 5):
        return("Sobota")
    elif(weekday == 6):
        return("Neděle")
    
def workDuration(start, end):
    # How many hours work took place in a single day
    work_duration_delta = end - start
    work_duration_seconds = work_duration_delta.total_seconds()
    work_duration_hours = work_duration_seconds / 3600

    if (work_duration_hours >= 4.5):
        return(work_duration_hours - 0.5)
    else:
        return(work_duration_hours)

def createTable(month, year, events_list):
    start_date = date(year=year, month=month, day=1)
    stop_date = date(year=year, month=month, day=calendar.monthrange(year, month)[1])
    date_list = dateRangeList(start_date, stop_date)
    
    table_list = []
    all_work = 0

    table_list.append(["<b>Datum</b>", "<b>Den</b>", "<b>Hodiny</b>"])
    table_list.append(["", "", ""])

    for date_unit in date_list:
        work = False
        for event in events_list:
            if (event[0].day == date_unit.day):
                #print(f"{date_unit}, {weekdayTranslate(date_unit.weekday())}: {workDuration(event[0],event[1])}")
                work_duration = workDuration(event[0],event[1])
                table_list.append([date_unit.strftime("%d.%m.%Y"), weekdayTranslate(date_unit.weekday()), work_duration])
                all_work += work_duration
                work = True
                break
        if not work:
            #print(f"{date_unit}, {weekdayTranslate(date_unit.weekday())}: -")
            table_list.append([date_unit.strftime("%d.%m.%Y"), weekdayTranslate(date_unit.weekday()), "-"])

    table_list.append(["","",""])
    table_list.append(["Celkem: ", "(h.)", all_work])
    table_list.append(["Výplata", "(Kč,-)", all_work*hourly_pay])
    
    table_html = '<table style="border-collapse: collapse;">\n'
    table_html += '  <colgroup>\n'
    table_html += '    <col style="width: 80px;">\n'
    table_html += '    <col style="width: 80px;">\n'
    table_html += '    <col style="width: 80px;">\n'
    table_html += '  </colgroup>\n'

    for row in table_list:
        if row[1] == "Sobota" or row[1] == "Neděle":
            table_html += '  <tr style="border: 1px solid black; background-color: green;">\n'
        else:
            table_html += '  <tr style="border: 1px solid black;">\n'
        for cell in row:
            table_html += f'    <td style="border: 1px solid black; text-align: center;">{cell}</td>\n'
        table_html += '  </tr>\n'

    table_html += '</table>'

    return(table_html)
    

if __name__ == '__main__':
    main()
