# FZJ-Weather Prometheus Exporter
The FZJ-Weather Prometheus Exporter (short: exporter) is an exporter compatible with the Prometheus database.
It consists of two parts:
  1. `fzj_weather.py`: a python script using BeautifulSoup4 and requests to parse and return meteorological data from a weather station inside of the Forschungszentrum Jülich (short: FZJ). It does so by parsing the website providing the information.
  2. exporter (`main.py`): uses said script to receive, parse and provide the data to the Prometheus database. Once started, it runs indefinetly until interrupt.

`main.py` references the weather script and other needed scripts. It therfore marks the entry point of the exporter.

# Exporter is currently under development
The exporter is not finished yet and full functionality is not guaranteed yet.

# Installing
TODO

# Testing:
To test the exporter, you can host the script on your own machine:
  1. `> python3 main.py`
  2. (from another terminal) `> curl 127.0.0.1:9840`

The default port in the script is 9840.
Running the second command should give you an output of similar structure like this:
```
# HELP fzj_weather_air_temperature temperature in celsius
# TYPE fzj_weather_air_temperature gauge
fzj_weather_air_temperature 14.0
```

(The output shoudl be similar for other data points, i.e. humidity)
