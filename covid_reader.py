import csv
import git
import mysql.connector
import decimal
import datetime
import json
from datetime import timedelta
from datetime import date
import os

from pytz import timezone

    
def ajax_is_the_worst():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    pact = {}
    pcon = {}
    prec = {}
    pdth = {}
    datapath = '/home/ubuntu/environment/project/covid_data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'
    filez = 0
    d2 = datetime.date(2020, 3, 22)
    
    for file in sorted(os.listdir(datapath)):
        filez += 1
        print(file)
        if filez > 61 and file[-4:] == ".csv":
            csvfile = os.path.join(datapath, file)
            with open(csvfile) as hfile:
                reader = csv.DictReader(hfile)
                counter = 0
                for row in reader:
                    fips = row['FIPS']
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
                #     #print('post except')
                #       #print(act)
                    deaths = row['Deaths']
                    confirmed = row['Confirmed']
                    recovered = row['Recovered']
                    active = row['Active']
                    daily_deaths = int(deaths) - dth
                    daily_confirmed = int(confirmed) - con
                    daily_recovered = int(recovered) - rec
                    daily_active = int(active) - act
                    sql = "INSERT INTO DailyReport (CountyFIPS, City, State, " \
                          "Date, Confirmed, Deaths, Recovered, Active) " \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    if counter < 5 and filez == 62:
                        print(sql%(row['FIPS'], row['Admin2'], row['Province_State'], d2.strftime('%Y-%m-%d'), daily_confirmed, daily_deaths, daily_recovered, daily_active))
                    try:
                        if row['FIPS'] == "":
                            continue
                        mycursor.execute(sql,(row['FIPS'], row['Admin2'], row['Province_State'], d2.strftime('%Y-%m-%d'), daily_confirmed, daily_deaths, daily_recovered, daily_active))
                    except mysql.connector.IntegrityError as err:
                        pass  
                    pact[fips] = int(active)
                    pcon[fips] = int(confirmed)
                    prec[fips] = int(recovered)
                    pdth[fips] = int(deaths)
                    counter += 1
            d2 += timedelta(days = 1)

                
    mydb.commit()

