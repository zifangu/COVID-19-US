import mysql.connector
import decimal
import datetime
import json
from datetime import timedelta
from datetime import date
# from datetime import datetime
from pytz import timezone

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}



mydb = mysql.connector.connect(
      host="localhost",
      user="ivan",
      passwd="helloworld",
      database="covid19"
    )
    
    
mycursor = mydb.cursor()
    
def DontTouch():
    mydb = mysql.connector.connect(
      host="localhost",
      user="ivan",
      passwd="helloworld",
      database="covid19"
    )
    
    
    mycursor = mydb.cursor()
    mycursor.execute("select * from Hospitals limit 5")
    results = mycursor.fetchall()
    
    for row in results:
    	print(row)
	
	
# 	********************CHASE茶斯**********************

def fun_1():
  sql = 'select sum(deaths) as deaths from DailyReport'
  # date = datetime.datetime.now(timezone('US/Eastern')) - timedelta(days=1)
  # date = date.strftime('%Y%m%d')
  # mycursor.execute(sql % (date))
  mycursor.execute(sql)
  fetch = mycursor.fetchall()
  dataFx = []
  for row in fetch:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result

def fun_2(date):
  sql = 'select sum(deaths) as deaths from DailyReport where date <= "%s"'
  mycursor.execute(sql % (date))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result

def fun_3(date):
  sql = 'select sum(deaths) as deaths from DailyReport where date = "%s"'
  mycursor.execute(sql % (date))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result
  
def fun_4(state):
  sql = 'select sum(deaths) as deaths from DailyReport where state = "%s"'
  mycursor.execute(sql % (state))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result
  
def fun_5(state, date):
  sql = 'select sum(deaths) as deaths from DailyReport where state = "%s" and date <= "%s"'
  mycursor.execute(sql % (state, date))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result
  
def fun_6(state, date):
  sql = 'select sum(deaths) as deaths from DailyReport where state = "%s" and date = "%s"'
  mycursor.execute(sql % (state, date))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"deaths": dataFx[0]})
  return result

#   ********************SCOTT司各特********************

"""
13. [baseurl]/covid19/hospitals/<state>/: returns the total number of open hospitals in the
given state as a JSON dictionary with the single key "hospitals"
14. [baseurl]/covid19/hospitals/<fips>/: returns the total number of open hospitals in the
given FIPS code as a JSON dictionary with the single key "hospitals"
15. [baseurl]/covid19/beds/<state>/: returns the total number of open hospital beds in the
given state as a JSON dictionary with the single key "beds"
16. [baseurl]/covid19/beds/<fips>/: returns the total number of open hospital beds in the
given FIPS code as a JSON dictionary with the single key "beds"
17. [baseurl]/covid19/capacity/<state>: returns the capacity (as a percentage) of the given
state, where capacity is defined to be current active cases divided by open hospital
beds, as a JSON dictionary with the single key "capacity"
18. [baseurl]/covid19/capacity/<fips>: returns the capacity (as a percentage) of the given
FIPS code, where capacity is defined to be current active cases divided by open hospital
beds, as a JSON dictionary with the single key "capacity"

"""
def fun_13(state):
  sql = "select count(Status) as TotalOpen from Hospitals where Status = 'OPEN' and State = '%s'"
  # print(sql % state)
  mycursor.execute(sql % (state))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"hospitals": dataFx[0]})
  # print(result)
  return result
  
def fun_14(countyfips):
  sql = "select count(ObjectID) from Hospitals join Location on Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and Status = 'OPEN'"
  # print(sql % countyfips)
  mycursor.execute(sql % (countyfips))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"hospitals": dataFx[0]})
  # print(result)
  return result
  
def fun_15(num_beds):
  sql = "select sum(Beds) as Total_Beds from Hospitals where State = '%s' and Beds != '-999' and Status = 'OPEN'"
  # print(sql % num_beds)
  mycursor.execute(sql % (num_beds))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"beds": dataFx[0]})
  # print(result)
  return result

def fun_16(num_beds):
  sql = "select sum(beds) as TotalBeds from Hospitals join Location on Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and Status='open' and beds != '-999';"
  # print(sql % num_beds)
  mycursor.execute(sql % (num_beds))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"beds": dataFx[0]})
  # print(result)
  return result
  
def fun_17(state_abrev):
  sql = "select sum((active.sum / beds.sum) * 100) from (select sum(Active) as sum from DailyReport where State = '%s') as active, (select sum(Beds) as sum from Hospitals where State = '%s' and Status = 'OPEN' and Beds != '-999') as beds;"
  state_name = state_abrev
  for key in states.keys():
    if key == state_name:
      state_name = states[state_name]
  #print(state_name)
  #print(sql % (state_abrev, state_name))
  mycursor.execute(sql % (state_name, state_abrev))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"beds": dataFx[0]})
  #print(result)
  return result

def fun_18(county_fips):
  sql = "select sum((active.sum / beds.sum) * 100) from (select sum(Active) as sum from DailyReport where DailyReport.CountyFIPS = '%s') as active, (select sum(Beds) as sum from Hospitals join Location on Location.LocationID = Hospitals.LocationID where CountyFIPS = '%s' and Status = 'OPEN' and Beds != '-999') as beds;"
  #print(sql % (county_fips, county_fips))
  mycursor.execute(sql % (county_fips, county_fips))
  data = mycursor.fetchall()
  dataFx = []
  for row in data:
    dataFx.append(list(map(str, row)))
  result = json.dumps({"beds": dataFx[0]})
  #print(result)
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
    # test = today.strftime('%Y-%m-%d')
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
#fun_1()
#fun_2('2020-04-17')
#fun_3('2020-04-17')
#fun_4('New York')
#fun_5('New York', '2020-04-02')
#fun_6('New York', '2020-04-02')
#fun_17('CT')
#fun_7("Georgia")
#fun_8(36061, '2020-05-05')
#fun_13('CT')
# fun_9()
#fun_14('1015')
#fun_15('CT')
#fun_10('2020-04-20')
#fun_16('1013')
#fun_11('Georgia')
#fun_18('6073')
#fun_12('Georgia', '2020-05-05')
# fun_19('6073')
#fun_20('6073')