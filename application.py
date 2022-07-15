from ast import Str
from flask import Flask,request,render_template
from pycaret.datasets import get_data
from pycaret.regression import *

import pandas as pd


application = Flask(__name__)

#dataset=pd.read_csv('Solar_dataset.csv')
#data = dataset.sample(frac=0.9, random_state=786)
#data_unseen = dataset.drop(data.index)

#colum_list = data_unseen.columns
#print(colum_list)

#print("DEBUG PRINT.....")
#print(type(data_unseen))


#colum_list = ["Day of Year","Year","Month","Day","First Hour of Period","Is Daylight","Distance to Solar Noon","Average Temperature (Day)","Average Wind Direction (Day)","Average Wind Speed (Day)","Sky Cover","Visibility","Relative Humidity","Average Wind Speed (Period)","Average Barometric Pressure (Period)"]
#print(type(colum_list))
#data_unseen=[245,2008,9,1,16,True,0.296915,69,28,7.5,0,10.0,20,23.0,29.85]
#df = pd.DataFrame (data_unseen, colum_list)

#print("dataFrame created")

#print(df)

cols =  ['Day of Year','Year','Month','Day','First Hour of Period','Is Daylight','Distance to Solar Noon','Average Temperature (Day)','Average Wind Direction (Day)','Average Wind Speed (Day)','Sky Cover','Visibility','Relative Humidity','Average Wind Speed (Period)','Average Barometric Pressure (Period)']


records = [
       [245,2008,9,1,16,True,0.296915,69,28,7.5,0,10.0,20,23.0,29.85],
]

new_data = pd.DataFrame(data=records, columns=cols)



saved_final_lightgbm = load_model('Final_LightGBM Model_14July2022')
new_prediction = predict_model(saved_final_lightgbm,new_data)
new_prediction[new_prediction < 0] = 0
#print(new_prediction.head())



@application.route("/",methods=["GET","POST"])
def powerRediction():
    year = "Empty"
    month = "Empty"
    day = "Empty"
    
    firstHourPeriod = "Empty"
    dayLight = "Empty"
    solarNoon = "Empty"
    avgTemp = "Empty"
    avg_wDirectio = "Empty"
    avg_wSpeed = "Empty"
    sky_cover = "Empty"
    visibility = "Empty"
    rHumidity = "Empty"
    avgWSpeedP = "Empty"
    avgPPeriod = "Empty"

    power_generated = 0.0
    predict = "Empty"


    print(request.method)

    if request.method == "POST":
    
        if "year" in request.form:
            year = request.form["year"]
            

        if "month" in request.form:
            month = request.form["month"]

    
        if "month" in request.form:
            day = request.form["day"]

        if "month" in request.form:
            firstHourPeriod = request.form["first_hour"]

        if "month" in request.form:
            dayLight = request.form["Isdaylight"]

        if "month" in request.form:
            solarNoon = request.form["solarNoon"]

        if "month" in request.form:
            avgTemp = request.form["avg_temperature"]

        if "month" in request.form:
            avg_wDirectio = request.form["avg_windDirection"]

        if "month" in request.form:
            avg_wSpeed = request.form["avg_windSpeed"]

        if "month" in request.form:
            sky_cover = request.form["sky_cover"]

        if "month" in request.form:
            visibility = request.form["visibility"]

        if "month" in request.form:
            rHumidity = request.form["relativeHumidity"]

        if "month" in request.form:
            avgWSpeedP = request.form["avg_windSpeed_period"]

        if "month" in request.form:
            avgPPeriod = request.form["avg_pressure"]

        cols =  ['Day of Year','Year','Month','Day','First Hour of Period','Is Daylight','Distance to Solar Noon','Average Temperature (Day)','Average Wind Direction (Day)','Average Wind Speed (Day)','Sky Cover','Visibility','Relative Humidity','Average Wind Speed (Period)','Average Barometric Pressure (Period)']


        records = [
            [245,year,month,day,firstHourPeriod,True,solarNoon,avgTemp,avg_wDirectio,avg_wSpeed,0,visibility,rHumidity,avgWSpeedP,avgPPeriod],
        ]   

        new_data = pd.DataFrame(data=records, columns=cols)

        saved_final_lightgbm = load_model('Final_LightGBM Model_14July2022')
        new_prediction = predict_model(saved_final_lightgbm,new_data)
        #new_prediction[new_prediction < 0] = 0
        
        print(new_prediction.iloc[0,15])
        predict = new_prediction.iloc[0,15]
        print("Power Generated   : ",predict)

    return render_template("index.html",power_generated=predict)


if __name__ == "__main__":
    application.run(debug=True)