import csv
import mysql.connector


def NAICS_details():
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
        
        
def county_details():
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
        for row in reader:
            sql = "INSERT INTO CountyDetails (CountyFIPS, County) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['COUNTYFIPS'], row['COUNTY']))
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()


def state_details():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO StateDetails (ST_FIPS, State) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['ST_FIPS'], row['State']))
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()


def location():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO Location (Address, City, CountyFIPS, ST_FIPS, Country, ZIP, ZIP4) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            if row['COUNTYFIPS'] == 'NOT AVAILABLE':
                county_fips = None
            else:
                county_fips = row['COUNTYFIPS']
            try:
                mycursor.execute(sql, (
                row['ADDRESS'], row['CITY'], county_fips, row['ST_FIPS'], row['COUNTRY'], row['ZIP'], row['ZIP4']))
            except mysql.connector.IntegrityError as err:
                pass

    mydb.commit()


def hospitals():
    mydb = mysql.connector.connect(
        host="localhost",
        user="ivan",
        passwd="helloworld",
        database="covid19"
    )
    mycursor = mydb.cursor(prepared=True)
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO Hospitals (Name, Type, NAICS_CODE, Beds, Trauma, Helipad, StateID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            if row['ST_FIPS'] == 'NOT AVAILABLE':
                StateID = None
            else:
                StateID = row['ST_FIPS']
            mycursor.execute(sql, (
            row['NAME'], row['TYPE'], row['NAICS_CODE'], row['BEDS'], row['TRAUMA'], row['HELIPAD'], StateID))
        #            except WHATEVER_THE_ERROR_IS_FOR_DUPLICATE_KEY:
        #                pass
        mydb.commit()


def hospital_location():
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

