import csv
import mysql.connector

# connects to the database on AWS
mydb = mysql.connector.connect(
    host="localhost",
    user="ivan",
    passwd="helloworld",
    database="covid19"
)
mycursor = mydb.cursor(prepared=True)

def NAICS_details():
    """
    Creates NAICS table in Database covid19
    :return: None.
    """

    # clear NAICS table
    mycursor.execute("DELETE FROM NAICS")

    # read "Hospitals.csv"
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:

            # mysql command
            sql = "INSERT INTO NAICS (NAICS_Code, NAICS_Desc) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['NAICS_CODE'], row['NAICS_DESC']))

            # handle duplicate key in database
            except mysql.connector.IntegrityError as err:
                pass
        # commit the changes to database
        mydb.commit()
        
        
def county_details():
    """
    Creates CountyDetails table
    :return: None.
    """

    # clear CountyDetails table
    mycursor.execute("DELETE FROM CountyDetails")

    # read in csv file
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO CountyDetails (CountyFIPS, County) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['COUNTYFIPS'], row['COUNTY']))

            # duplicate key case handling
            except mysql.connector.IntegrityError as err:
                pass
        mydb.commit()


def state_details():
    """
    Creates StateDetails table
    :return: None.
    """

    # clear StateDetails table
    mycursor.execute("DELETE FROM StateDetails")

    # read in csv
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:
            sql = "INSERT INTO StateDetails (ST_FIPS, State) VALUES (%s, %s)"
            try:
                mycursor.execute(sql, (row['ST_FIPS'], row['State']))
            except mysql.connector.IntegrityError as err:
                pass

        # database commit
        mydb.commit()


def location():
    """
    Create Location table
    :return: None.
    """

    # read in csv
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:

            # sql insertion command
            sql = "INSERT INTO Location (Address, City, CountyFIPS, ST_FIPS, Country, ZIP, ZIP4) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            # For this database we are only handling continental US data.
            if row['COUNTYFIPS'] == 'NOT AVAILABLE':
                continue
            else:
                county_fips = row['COUNTYFIPS']
            try:
                mycursor.execute(sql, (
                row['ADDRESS'], row['CITY'], county_fips, row['ST_FIPS'], row['COUNTRY'], row['ZIP'], row['ZIP4']))

            # duplicate key handling
            except mysql.connector.IntegrityError as err:
                pass

    # commit to database
    mydb.commit()


def hospitals():
    """
    create Hopsitals table in database
    :return: None.
    """

    # read in csv
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)
        for row in reader:

            # mysql insertion command
            sql = "INSERT INTO Hospitals (Name, Type, NAICS_CODE, Beds, Trauma, Helipad, StateID) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"

            # skipping data outside of continental US
            if row['ST_FIPS'] == 'NOT AVAILABLE':
                continue
            else:
                StateID = row['ST_FIPS']

            # try catch block handling duplicate key
            try:
                mycursor.execute(sql, (
                row['NAME'], row['TYPE'], row['NAICS_CODE'], row['BEDS'], row['TRAUMA'], row['HELIPAD'], StateID))
            except mysql.connector.IntegrityError as err:
                pass

        # commit to database
        mydb.commit()


def hospital_location():
    """
    Connect Hospitals and Location tables
    :return:
    """

    # read in csv
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)

        # corresponds to each record in Location from Hospitals.csv. Auto-increment starts at 2245
        LOCATION_ID = 2245

        # each record in Hospitals is read from Hpsitals.csv where the autoincrement starts at 89
        OBJ_ID = 89
        for row in reader:

            # fill in the foreign key column LOCATION_ID in Hospitals to connect with primary key column in Locations
            sql = "UPDATE Hospitals set LOCATION_ID = %s where ObjectID = %s" % (LOCATION_ID, OBJ_ID)

            # handle duplicate keys
            try:
                mycursor.execute(sql)
            except mysql.connector.IntegrityError as err:
                pass

            # increment both IDs
            LOCATION_ID += 1
            OBJ_ID += 1

        # commit to database
        mydb.commit()


def hospitals_status():
    """
    modify Hospitals to include STATUS information (OPEN/CLOSED)
    :return: None.
    """

    # read in csv file
    with open('Hospitals.csv') as hfile:
        reader = csv.DictReader(hfile)

        # each record in Hospitals is read from Hpsitals.csv where the autoincrement starts at 89
        OBJ_ID = 89
        for row in reader:
            Status = row['STATUS']
            sql = "UPDATE Hospitals set Status = '%s' where ObjectID = %s" % (Status, OBJ_ID)

            # duplicate key handling
            try:
                mycursor.execute(sql)
            except mysql.connector.IntegrityError as err:
                pass
            OBJ_ID += 1

        # commit to database
        mydb.commit()

