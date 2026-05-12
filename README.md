## F1Stats: v1
We created a dashboard to visualize pseudo live telemetry from F1 race. Yes, we did not know anything about F1 before this!

Formula One (F1) is the top level of single-seater motor racing held on circuits worldwide. Each Grand Prix covers around 305 km, completed over multiple laps (usually 50–70, depending on the track length). The race weekend includes practice sessions, qualifying to decide grid positions, and the main race.

This project involves a dashboard that visualizes live telemetry from Formula One racing cars. **The data is collected from the FastF1 API**. **Grafana Cloud is used for visualizing the stats of 1 lap in a session.**

Currently the telemetry data that is used in the project:

* Lap details: Weather at the circuit
* Car details: Position(X,Y Coordinates), Speed,Throttle,Relative Distance,Gear Shifts, Driver name

Visualizations:
* Top 3 drivers at any time and their relative distances
* Position plot(XY Plot), Speed vs Time,Throttle vs Time,Gear Shift vs Time
* Weather data for the selected lap

**The data for the competing drivers in a particular lap is sent simultaneously with associated race delays through Python to InfluxDB**, the intermediary between Grafana Cloud and Python. 

The data required is queried periodically and the live data is then displayed using Grafana Cloud, which updates the visuals instantly as new data arrives from InfluxDB.

 Viewers can easily see key information such as the speed, throttle, positions, gear shifts and top 3 drivers at any time, their relative distances from the end of the lap, and changes over time, all presented through interactive charts and panels.


 PS: We are working on the second version. Stay tuned.
