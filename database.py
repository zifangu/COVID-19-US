import csv
import mysql.connector
# file = open('Hospitals.csv')
# reader = csv.DictReader(file)

# counter = 0
# for row in reader:
#     if counter < 10:
#         print(row["CITY"])     
#     counter += 1
    
    
def NAICS_DESCRIPTION():
       
    with open('Hospitals.csv', mode='r') as file1:
        reader = csv.DictReader(file1)
        # *********NAICS CODE*********
        with open('NAICS_DETAILS.csv', mode='w') as file2:
            fieldname = ['X','Y','OBJECTID','ID','NAME','ADDRESS']
            # 'CITY','STATE','ZIP','ZIP4',TELEPHONE,TYPE,STATUS,POPULATION,COUNTY,COUNTYFIPS,COUNTRY,LATITUDE,LONGITUDE,NAICS_CODE,NAICS_DESC,SOURCE,SOURCEDATE,VAL_METHOD,VAL_DATE,WEBSITE,STATE_ID,ALT_NAME,ST_FIPS,OWNER,TTL_STAFF,BEDS,TRAUMA,HELIPAD]
            writer = csv.DictWriter(file2, fieldnames=fieldname)
            # dict = {'NAICS_CODE':row['NAICS_CODE'], 'NAICS_DESC':row['NAICS_DESC']}
            dict = {}
            naics_val = []
            sql_ready = []
            for row in reader:
                dict['NAICS_CODE'] = row['NAICS_CODE']
                if dict.get('NAICS_CODE') not in naics_val:
                #     dict['NAICS_CODE'] = row['NAICS_CODE']
                # if dict.get('NAICS_DESC') is None:
                #     dict['NAICS_DESC'] = row['NAICS_DESC']
                    naics_val.append(dict.get('NAICS_CODE'))
                    sql_ready.append((row['NAICS_CODE'],row['NAICS_DESC']))
                    # writer.writerow({'NAICS_CODE':row['NAICS_CODE'], 'NAICS_DESC':row['NAICS_DESC']})
                    # dict['NAICS_CODE'] = row['NAICS_CODE']
                    # dict['NAICS_DESC'] = row['NAICS_DESC']
            # file2.close()
            print(sql_ready)
    return sql_ready
    
    
    
    file = open('Hospitals.csv')
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if counter < 1:
            print(row, "\n")
        counter += 1
    

def garrett_is_the_best():
    # NAICS details
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    mycursor.execute("DELETE FROM NAICS")
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO NAICS (NAICS_Code, NAICS_Desc) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['NAICS_CODE'], row['NAICS_DESC']))
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()
        
        
def ivan_is_the_best():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    mycursor.execute("DELETE FROM CountyDetails")
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        counter = 0
        for row in reader:
            sql = "INSERT INTO CountyDetails (CountyFIPS, County) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['COUNTYFIPS'], row['COUNTY']))
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()
        
def zifan_is_the_best():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    mycursor.execute("DELETE FROM DailyReport")
    with open('~/environment/project/covid_data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/04-25-2020.csv') as hfile:
        reader = csv.DictReader(hfile)
        counter = 0
        for row in reader:
            sql = "INSERT INTO CountyDetails (CountyFIPS, City, State, Daate, Confirmed, Deaths, Recovered, Active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                temp_date = "2020-04-25"
                mycursor.execute(sql, (row['FIPS'], row['Admin2'], row['Province_State'], temp_date, row['Confirmed'], row['Deaths'], row['Recovered'], row['Active']))
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()


def banks_is_the_best():
    # state details
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        count = 0
        for row in reader:
            if count < 20:
               print(row['ST_FIPS'], row['STATE'])
            count += 1
    



def db_write():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM NAICS")
    # ~/home/ubuntu/environment/project/
    # mycursor.execute("CREATE TABLE NAICS_DETAILS (NAICS_CODE VARCHAR(255), NAICS_DESC VARCHAR(255))")
    
    
    
    #with open('Hospitals.csv') as hfile:
        
        
    sql = "INSERT INTO NAICS (NAICS_CODE, NAICS_DESC) VALUES (%s, %s)"
    
    cmd = "LOAD DATA LOCAL INFILE '~//home/ubuntu/environment/project/Hospitals.csv' INTO TABLE temp COLUMNS TERMINATED BY ','"
    # sql_ready = NAICS_DESCRIPTION()
    # mycursor.executemany(sql, sql_ready)
    mycursor.execute(cmd)
    mydb.commit()
    
    print(mycursor.rowcount, "was inserted.")
             
def ivan_save_the_day():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        ID = 2245
        OBJ_ID = 89
        for row in reader:
            sql = "UPDATE Hospitals set ID = %s where ObjectID = %s" % (ID, OBJ_ID)
            try:
                mycursor.execute(sql)
            except mysql.connector.IntegrityError as err:
                pass
            ID += 1
            OBJ_ID += 1
        # print(sql)
        mydb.commit()

def zifan_save_the_day():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        OBJ_ID = 89
        counter = 0
        for row in reader:
            State = row['STATE']
            if counter < 5:
                print(State)
            sql = "UPDATE Hospitals set State = '%s' where ObjectID = %s" % (State, OBJ_ID)
            try:
                # print(sql)
                mycursor.execute(sql)
            except mysql.connector.IntegrityError as err:
                pass
            OBJ_ID += 1
            counter += 1
        # print(sql)
        mydb.commit()
        
        
        
        
        
        
        

def Hospitals_Status():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        OBJ_ID = 89
        counter = 0
        for row in reader:
            Status = row['STATUS']
            if counter < 5:
                print(Status)
            sql = "UPDATE Hospitals set Status = '%s' where ObjectID = %s" % (Status, OBJ_ID)
            try:
                # print(sql)
                mycursor.execute(sql)
            except mysql.connector.IntegrityError as err:
                pass
            OBJ_ID += 1
            counter += 1
        # print(sql)
        mydb.commit()

# garrett_is_the_best()
# ivan_is_the_best()
# banks_is_the_best()
# ivan_save_the_day()
# zifan_is_the_best()
#NAICS_DESCRIPTION()
# db_write()
Hospitals_Status()
#zifan_save_the_day()

