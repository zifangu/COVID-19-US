import csv
import mysql.connector
import datetime
import json
from datetime import timedelta
from datetime import date
import os

from pytz import timezone

    
def daily_report_initialize():
    """
    Function call to initialize "DailyReport" table in the "covid19" database
    :return: None.
    """

    # connects to the database on AWS
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)

    # empty dictionary used to store previous active, confirmed, recovered, and deaths
    pact = {}
    pcon = {}
    prec = {}
    pdth = {}
    datapath = '/home/ubuntu/environment/project/covid_data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'
    filez = 0

    # March 22, 2020 is the initial date by group choice
    d1 = datetime.date(2020, 3, 22)
    
    for file in sorted(os.listdir(datapath)):

        # after sorting the directory, the 61st file with .csv extension is 03-22-2020.csv
        if filez > 60 and file[-4:] == ".csv":
            csvfile = os.path.join(datapath, file)
            with open(csvfile) as hfile:
                reader = csv.DictReader(hfile)
                counter = 0
                for row in reader:
                    fips = row['FIPS'] # read in FIPS from file

                    # if dictionary is empty, set previous values to 0. Else, load the stored value
                    try:         
                        act = pact[fips]
                        con = pcon[fips]
                        rec = prec[fips]
                        dth = pdth[fips]
                    except KeyError:
                        act = 0
                        con = 0
                        rec = 0
                        dth = 0

                    # read the daily cumulative count from file
                    deaths = row['Deaths']
                    confirmed = row['Confirmed']
                    recovered = row['Recovered']
                    active = row['Active']

                    # adjust to record true daily counts
                    daily_deaths = int(deaths) - dth
                    daily_confirmed = int(confirmed) - con
                    daily_recovered = int(recovered) - rec
                    daily_active = int(active) - act

                    # mysql statement to insert records into table "DailyReport"
                    sql = "INSERT INTO DailyReport (CountyFIPS, City, State, " \
                          "Date, Confirmed, Deaths, Recovered, Active) " \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                    # For this database we are only handling continental US.
                    # If no FIPS is recorded, the row represents either international or territories, skips that row.
                    try:
                        if row['FIPS'] == "":
                            continue

                        # execute the sql statement
                        mycursor.execute(sql, (row['FIPS'], row['Admin2'], row['Province_State'], d1.strftime('%Y-%m-%d'), daily_confirmed, daily_deaths, daily_recovered, daily_active))

                    # if duplicate key, pass
                    except mysql.connector.IntegrityError as err:
                        pass

                    # replace the previous daily count dictionary with today's value
                    pact[fips] = int(active)
                    pcon[fips] = int(confirmed)
                    prec[fips] = int(recovered)
                    pdth[fips] = int(deaths)
                    counter += 1

            # read in the next day file.
            d1 += timedelta(days=1)
        filez += 1

    # commit the database change
    mydb.commit()

def daily_report_update():
    return 0

