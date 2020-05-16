# COVID-19-US

This project is a collaboration between my two teammates. We implemented this in AWS therefore it cannot be run directly by cloning this repo. It is meant to be used as a demonstration of skills or knowledge on normalizing database, Flask, and AJAX.

The Database is 3NF created using raw data from Johns Hopkins Wighting School of Engeering Github repo: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

The numbers in that repo are cumulative. In our database, we modified the data to contain the true daily counts, not the cumulative counts.

Flask handles GET requests for COVID-19 active/deaths. Examples requests: [baseurl]/covid19/deaths/<fips>/<date>: returns the number of deaths in the FIPS code on the given date as a JSON dictionary with the single key "deaths."
  
AJAX client set up: allows a GET request that takes a given FIPS code, producting two of the following charts. The first is a line chart that shows the
historical COVID-19 deaths in that FIPS code starting from March 22, 2020, to the present. The
second is a line chart that shows the historical active cases in that FIPS code starting from
March 22, 2020, to the present, along with a horizontal line marking the total number of open
hospital beds in that FIPS code.

The reason we chose March 22, 2020 as our starting date is based on consisent formating in the daily report files and significance of case numbers. 
