import mysql.connector
from FlaskApp import app
from FlaskApp import paths
from markupsafe import escape
from flask_call import render_template



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
   return paths.death_cumulative()
@app.route('/covid19/deaths/cumulative/<int:date>')
def cumulativedate(date):
    return paths.death_cumulative_date(date)

@app.route('/covid19/deaths/<int:date>')
def death_date(date):
    return paths.deaths_single_day(date)

@app.route('/covid19/deaths/<state>/cumulative')
def state_cumulative(state):
    return paths.deaths_cumulative_state(state)

@app.route('/covid19/deaths/<state>/cumulative/<int:date>')
def state_cumulative_date(state, date):
    return paths.deaths_cumulative_state_date(state, date)

@app.route('/covid19/deaths/<state>/<int:date>')
def death_state_date(state, date):
    return paths.deaths_single_day_state_date(state, date)
   
   
#***************************************Daddy************************************

@app.route('/covid19/hospitals/<state>')
def Open_Hospitals(state):
    return paths.hospitals_open(state)
    
@app.route('/covid19/hospitals/<int:fips>')
def FIPS_Open_Hospitals(fips):
    return paths.hospitals_open_fips(fips)

@app.route('/covid19/beds/<state>')
def Open_Beds(state):
    return paths.beds_open_state(state)
    
@app.route('/covid19/beds/<int:fips>')
def FIPS_Open_Beds(fips):
    return paths.beds_open_fips(fips)
    
@app.route('/covid19/capacity/<state>')
def State_Capacity(state):
    return paths.capacity_state(state)
    
@app.route('/covid19/capacity/<int:fips>')
def FIPS_Capacity(fips):
    return paths.capacity_fips(fips)
    
    
    

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


