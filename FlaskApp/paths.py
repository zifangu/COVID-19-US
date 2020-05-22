import mysql.connector
import decimal
import datetime
import json
from datetime import timedelta
from datetime import date
# from datetime import datetime
from pytz import timezone

# dictionary to convert state abbreviation to full name
states = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California',
          'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida',
          'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana',
          'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine',
          'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi',
          'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',
          'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon',
          'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
          'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin',
          'WV': 'West Virginia', 'WY': 'Wyoming'}

# connect to database on AWS
mydb = mysql.connector.connect(
      host="localhost",
      user="ivan",
      passwd="helloworld",
      database="covid19"
    )

# set database cursor
mycursor = mydb.cursor()


# 	********************CHASE茶斯**********************

def death_cumulative():
    """
    :return: the total number of deaths in the U.S. up to
the present as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport'
    mycursor.execute(sql)

    # fetch the result from sql command and append to a list
    fetch = mycursor.fetchall()
    dataFx = []
    for row in fetch:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result


def death_cumulative_date(date):
    """
    :param date: in the format YYYYMMDD
    :return: the total number of deaths in the
U.S. up to the given date as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport where date <= "%s"'
    mycursor.execute(sql % (date))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result


def deaths_single_day(date):
    """
    :param date: formatted YYYYMMDD
    :return: returns the number of deaths in the U.S. on the given
date as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport where date = "%s"'
    mycursor.execute(sql % (date))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result


def deaths_cumulative_state(state):
    """
    :param state: a US state (full name), territories, or Grand Princess
given state up to the present as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport where state = "%s"'
    mycursor.execute(sql % (state))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result


def deaths_cumulative_state_date(state, date):
    """
    :param state: a US state (full name), territories, or Grand Princess
    :param date: formatted YYYYMMDD
    :return: returns the total number of deaths
in the given state up to the given date as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport where state = "%s" and date <= "%s"'
    mycursor.execute(sql % (state, date))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result

  
def deaths_single_day_state_date(state, date):
    """
    :param state: a US state (full name), territories, or Grand Princess
    :param date: formatted YYYYMMDD
    :return: returns the number of deaths in the given state
on the given date as a JSON dictionary with the single key "deaths"
    """

    # sql command
    sql = 'select sum(deaths) as deaths from DailyReport where state = "%s" and date = "%s"'
    mycursor.execute(sql % (state, date))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "deaths"
    result = json.dumps({"deaths": dataFx[0]})
    return result

#   ********************SCOTT********************


def hospitals_open(state):
    """
    :param state: a US state or territories (in abbreviation form)
    :return:  the total number of open hospitals in the
given state as a JSON dictionary with the single key "hospitals"
    """

    # sql command
    sql = "select count(Status) as TotalOpen from Hospitals where Status = 'OPEN' and State = '%s'"
    mycursor.execute(sql % state)

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "hospitals"
    result = json.dumps({"hospitals": dataFx[0]})
    return result


def hospitals_open_fips(countyfips):
    """
    :param countyfips: a five-digit Federal Information Processing Standards code
    which uniquely identified counties in the United States
    :return:  the total number of open hospitals in the
given FIPS code as a JSON dictionary with the single key "hospitals"
    """

    # sql command
    sql = "select count(ObjectID) from Hospitals join Location on " \
          "Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and Status = 'OPEN'"
    mycursor.execute(sql % countyfips)

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "hospitals"
    result = json.dumps({"hospitals": dataFx[0]})
    return result


def beds_open_state(state):
    """
    :param state: a US state or territories (in abbreviation form)
    :return: the total number of open hospital beds in the
given state as a JSON dictionary with the single key "beds"
    """

    # sql command
    # Hospitals.csv convention when beds = -999 there are no beds available
    sql = "select sum(Beds) as Total_Beds from Hospitals where State = '%s' and Beds != '-999' and Status = 'OPEN'"
    mycursor.execute(sql % state)

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "beds"
    result = json.dumps({"beds": dataFx[0]})
    # print(result)
    return result


def beds_open_fips(fips):
    """
    :param fips: a five-digit Federal Information Processing Standards code
    which uniquely identified counties in the United States
    :return: the total number of open hospital beds in the
given FIPS code as a JSON dictionary with the single key "beds"
    """

    # sql command
    sql = "select sum(beds) as TotalBeds from Hospitals join Location on " \
          "Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and Status='open' and beds != '-999';"
    mycursor.execute(sql % fips)

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "beds"
    result = json.dumps({"beds": dataFx[0]})
    return result

  
def capacity_state(state):
    """
    :param state: a US state or territories (in abbreviation form)
    :return: the capacity (as a percentage) of the given state, where capacity is defined to be current active cases divided by open hospital
beds, as a JSON dictionary with the single key "capacity"
    """

    # sql command
    sql = "select sum((active.sum / beds.sum) * 100) from (select sum(Active) as sum " \
          "from DailyReport where State = '%s') as active, (select sum(Beds) as sum from Hospitals " \
          "where State = '%s' and Status = 'OPEN' and Beds != '-999') as beds;"

    # convert state from abbreviation to full name
    state_name = None
    for key in states.keys():
        if key == state_name:
            state_name = states[state_name]

    # fetch the result from sql command and append to a list
    mycursor.execute(sql % (state_name, state))
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "capacity"
    result = json.dumps({"capacity": dataFx[0]})
    return result


def capacity_fips(county_fips):
    """
    :param county_fips: a five-digit Federal Information Processing Standards code
    which uniquely identified counties in the United States
    :return: the capacity (as a percentage) of the given FIPS code, where capacity is defined to be current active cases divided by open hospital
beds, as a JSON dictionary with the single key "capacity"
    """

    # sql command
    sql = "select sum((active.sum / beds.sum) * 100) from (select sum(Active) as sum from " \
          "DailyReport where DailyReport.CountyFIPS = '%s') as active, (select sum(Beds) as sum from " \
          "Hospitals join Location on Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and " \
          "Status = 'OPEN' and Beds != '-999') as beds;"
    mycursor.execute(sql % (county_fips, county_fips))

    # fetch the result from sql command and append to a list
    data = mycursor.fetchall()
    dataFx = []
    for row in data:
        dataFx.append(list(map(str, row)))

    # creates JSON dictionary with the single key "capacity"
    result = json.dumps({"beds": dataFx[0]})
    return result



#   *********************Ivan子凡**************************

"""
7. [baseurl]/covid19/deaths/<state>: returns a JSON dictionary (key is the date in
MMDDYYYY format) of deaths each day for the given state
8. [baseurl]/covid19/deaths/<fips>/<date>: returns the number of deaths in the FIPS code
on the given date as a JSON dictionary with the single key "deaths"
9. [baseurl]/covid19/cases: returns the total number of active cases in the U.S. on the
present date as a JSON dictionary with the single key "active"
10. [baseurl]/covid19/cases/<date>: returns the total number of active cases in the U.S. on
the given date as a JSON dictionary with the single key "active"
11 [baseurl]/covid19/cases/<state>: returns the total number of active cases in the given
state on the present date as a JSON dictionary with the single key "active"
12. [baseurl]/covid19/cases/<state>/<date>: returns the total number of active cases in the
given state on the given date as a JSON dictionary with the single key "active"
"""

def fun_7(state):
    sql = "select Date, sum(Deaths) from DailyReport where State = '%s' and Date = '%s'" 
    d1 = datetime.date(2020, 3, 22)
    today = datetime.datetime.now(timezone('US/Eastern'))
    # today = date.today() - timedelta(days=1)
    print(today)
    
    result = []
    while (today.date() > d1):
        # date_para = d1.strftime('%m-%d-%Y')
        # print(sql % (state, d1))
        d1_str = d1.strftime('%Y-%m-%d')
        # print(sql % (state, d1))
        mycursor.execute(sql % (state, d1))
        temp = mycursor.fetchall()
        for row in temp:
          result.append(row)
        # result.append(mycursor.fetchall)
        # print(results)
        d1 += timedelta(days=1)
    
    json_dict = {}
    for i in result:
      # print(i[1])
      json_dict[i[0].strftime('%m-%d-%Y')] = int(i[1])
    # print(json_dict)
    return json.dumps(json_dict)
    
def fun_8(fips, date):
  sql = "select sum(Deaths) from DailyReport where CountyFIPS = '%s' and Date = '%s'"
  print(sql % (fips, date))
  mycursor.execute(sql % (fips, date))
  json_dict = {}
  for i in mycursor.fetchall():
    json_dict['deaths'] = int(i[0])
  return json.dumps(json_dict)
  
def fun_9():
  today = datetime.datetime.now(timezone('US/Eastern')).date() - timedelta(days=1)
  
  d1 = datetime.date(2020, 3, 22)
  sql = "select sum(Active) from DailyReport"
  # print(sql % today.strftime('%Y-%m-%d') )
  mycursor.execute(sql)
    
  result = mycursor.fetchall()
  # while (today > d1):
  #     d1_str = d1.strftime('%Y-%m-%d')
  #     mycursor.execute(sql % (d1))
  #     temp = mycursor.fetchall()
  #     for row in temp:
  #       result.append(row)
  #     d1 += timedelta(days=1)
  # total = 0
  # for i in result:
  #   total += int(i[0])
  json_dict = {}
  json_dict["active"] = int(result[0][0])
  # print(result[0][0])
  return json.dumps(json_dict)
   
  
def fun_10(date):
  sql = "select sum(Active) from DailyReport where Date <= '%s'"
  print(sql % date)
  mycursor.execute(sql % date)
  json_dict = {}
  for i in mycursor.fetchall():
    json_dict['active'] = int(i[0])
  return json.dumps(json_dict)
  
def fun_11(state):
    today = datetime.datetime.now(timezone('US/Eastern')).date() - timedelta(days=1)
    sql = "select sum(Active) from DailyReport where State = '%s'"
    # death_cumulative = today.strftime('%Y-%m-%d')
    print(sql %  state)
    mycursor.execute(sql % state)
    json_dict = {}
    for i in mycursor.fetchall():
      json_dict['active'] = int(i[0])
    return json.dumps(json_dict)
    
def fun_12(state, date):
  sql = "select sum(Active) from DailyReport where state = '%s' and Date <= '%s'"
  print(sql % (state, date))
  mycursor.execute(sql % (state, date))
  json_dict = {}
  for i in mycursor.fetchall():
    json_dict['active'] = int(i[0])
  return json.dumps(json_dict)
  
  
#****************Ajax Functions****************


def fun_19(county_fips):
  sql = "select Deaths, Date from DailyReport where CountyFIPS = '%s'"
  #print(sql % county_fips)
  mycursor.execute(sql % (county_fips))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"Deaths": dataFx})
  #print(result)
  return (result)
  
  
  
def fun_20(county_fips):
  sql = "select Active, Date from DailyReport where CountyFIPS = '%s'"
  #print(sql % county_fips)
  mycursor.execute(sql % (county_fips))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
    print(row[1])
  result = json.dumps({"Active": dataFx})
  #print(result)
  return (result)
  
  
  
def ajax_death(fips):
    sql = "select Date, sum(Deaths) from DailyReport where CountyFIPS = '%s' and Date = '%s'" 
    d1 = datetime.date(2020, 3, 22)
    today = datetime.datetime.now(timezone('US/Eastern'))
    # today = date.today() - timedelta(days=1)
    print(today)
    
    result = []
    while (today.date() > d1):
        d1_str = d1.strftime('%Y-%m-%d')
        mycursor.execute(sql % (fips, d1))
        temp = mycursor.fetchall()
        for row in temp:
          result.append(row)
        d1 += timedelta(days=1)
    
    json_dict = {}
    for i in result:
      # print(i[1])
      json_dict[i[0].strftime('%m-%d-%Y')] = int(i[1])
    # print(json_dict)
    return json.dumps(json_dict)
  
  
  
  
    
  # print(today)
  

# *************function calls************

# ajax_death(45083)
#death_cumulative()
#death_cumulative_date('2020-04-17')
#deaths_single_day('2020-04-17')
#deaths_cumulative_state('New York')
#deaths_cumulative_state_date('New York', '2020-04-02')
#deaths_single_day_state_date('New York', '2020-04-02')
#capacity_state('CT')
#fun_7("Georgia")
#fun_8(36061, '2020-05-05')
#hospitals_open('CT')
# fun_9()
#hospitals_open_fips('1015')
#beds_open_state('CT')
#fun_10('2020-04-20')
#beds_open_fips('1013')
#fun_11('Georgia')
#capacity_fips('6073')
#fun_12('Georgia', '2020-05-05')
# fun_19('6073')
#fun_20('6073')