import mysql.connector
from app import app
from app import paths
from markupsafe import escape
from flask import render_template



mydb = mysql.connector.connect(
      host="localhost",
      user="ivan",
      passwd="helloworld",
      database="covid19"
    )
mycursor = mydb.cursor()


@app.route("/")

def hello():
    return render_template("index.html")
    
@app.route("/covid19/ajax")
def ajax():
    return render_template("ajax.html")

@app.route('/covid19/deaths/cumulative')
def cumulative():
   return paths.fun_1()
@app.route('/covid19/deaths/cumulative/<int:date>')
def cumulativedate(date):
    return paths.fun_2(date)

@app.route('/covid19/deaths/<int:date>')
def death_date(date):
    return paths.fun_3(date)

@app.route('/covid19/deaths/<state>/cumulative')
def state_cumulative(state):
    return paths.fun_4(state)

@app.route('/covid19/deaths/<state>/cumulative/<int:date>')
def state_cumulative_date(state, date):
    return paths.fun_5(state, date)

@app.route('/covid19/deaths/<state>/<int:date>')
def death_state_date(state, date):
    return paths.fun_6(state, date)
   
   
#***************************************Daddy************************************

@app.route('/covid19/hospitals/<state>')
def Open_Hospitals(state):
    return paths.fun_13(state)
    
@app.route('/covid19/hospitals/<int:fips>')
def FIPS_Open_Hospitals(fips):
    return paths.fun_14(fips)

@app.route('/covid19/beds/<state>')
def Open_Beds(state):
    return paths.fun_15(state)
    
@app.route('/covid19/beds/<int:fips>')
def FIPS_Open_Beds(fips):
    return paths.fun_16(fips)
    
@app.route('/covid19/capacity/<state>')
def State_Capacity(state):
    return paths.fun_17(state)
    
@app.route('/covid19/capacity/<int:fips>')
def FIPS_Capacity(fips):
    return paths.fun_18(fips)
    
    
    

# *************************************Mommy***********************************

@app.route('/covid19/deaths/<state>')
def cases_date(state):
    return paths.fun_7(state)

@app.route('/covid19/deaths/<int:fips>/<int:date>')
def fips_date(fips, date):
    return paths.fun_8(fips, date)
    
@app.route('/covid19/cases')
def cases():
    return paths.fun_9()
    
@app.route('/covid19/cases/<int:date>')
def date_case(date):
    return paths.fun_10(date)
    
@app.route('/covid19/cases/<state>')
def state_case(state):
    return paths.fun_11(state)
    
@app.route('/covid19/cases/<state>/<int:date>')
def state_date_case(state, date):
    return paths.fun_12(state, date)
    
#*******************Ajax Routes******************

@app.route('/covid19/span/deaths/<int:county_fips>')
def span_deaths(county_fips):
    return paths.fun_19(county_fips)

@app.route('/covid19/span/active/<int:county_fips>')
def span_active(county_fips):
    return paths.fun_20(county_fips)
    
    
@app.route('/covid19/foo/death/<int:county_fips>')    
def foo_death(county_fips):
    return paths.ajax_death(county_fips)


