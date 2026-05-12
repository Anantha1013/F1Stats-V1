import paho.mqtt.client as mqtt
import json
import fastf1
import time
import os, time, datetime
from influxdb_client_3 import InfluxDBClient3, Point
import threading as th
from datetime import timedelta

def send_data(telemetry,driver):
    delayTime=0.5
    for i in range(2, len(telemetry)):
        json_object = {
            "X": float(telemetry.loc[i,"X"]),
            "Y": float(telemetry.loc[i,"Y"]),
            "DriverName": driver,
            "Speed": float(telemetry.loc[i,"Speed"]),
            "GearShift": float(telemetry.loc[i,"nGear"]),
            "DRS": float(telemetry.loc[i,"DRS"]),
            "Brake": (telemetry.loc[i,"Brake"]),
            "Throttle": float(telemetry.loc[i,"Throttle"]),
            "Distance": float(telemetry.loc[i,"Distance"]),
            "RelativeDistance": float(telemetry.loc[i,"RelativeDistance"])
        }

        point1 = (
    Point("Telemetry")
    .tag("driver", json_object["DriverName"])
    .field("driverName", json_object["DriverName"])
    .field("x", (json_object["X"]))  
    .field("y", (json_object["Y"]))  
    .field("speed",(json_object["Speed"]))
    .field("gearShift",(json_object["GearShift"]))
    .field("drs",(json_object["DRS"]))
    .field("brake",str(json_object["Brake"]))
    .field("throttle",(json_object["Throttle"]))
    .field("distance",(json_object["Distance"]))    
    .field("relativeDistance",(json_object["RelativeDistance"]))
)
        
        if(i!=len(tele_data)-1):
        
            time1 = tele_data.loc[i,"Time"]
            time2 = tele_data.loc[i+1,"Time"]
            delayTime=(time2-time1).total_seconds()




        client.write(database=database, record=point1)
        time.sleep(delayTime)

        print(json_object)

    





token = "<Influx db token>"
org = "F1 visualization"
host = "https://eu-central-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)

database="TelemetryOfCars"

session = fastf1.get_session(2023, 1, 'R')
session.load()
driver_laps = session.laps
#tel=driver_laps.get_telemetry()

#print(session.drivers)

#lap=driver_laps.pick_driver(11)
#print(lap['Position'])
driverThreads=[]
for i in session.drivers:
     lap=driver_laps.pick_driver(i).pick_lap(2)
     tele_data=lap.get_telemetry()
     driverRecord=th.Thread(target=send_data,args=(tele_data,driver_laps.pick_driver(i).iloc[0,1]))
     driverThreads.append(driverRecord)
     driverRecord.start()
   
     

for thread in driverThreads:
    thread.join()