#!/usr/bin/env python3

from dataclasses import dataclass
from fzj_weather import main as get_weather_data


@dataclass
class Weather:
    temperature: float  # celsius
    air_pressure: float  # hectoPascal
    humidity: int  # percent
    wind_power: int  # beaufort
    wind_direction: int  # degree
    velocity_ms: float  # m/s
    velocity_kmh: float  # km/h


def fzj_weather_crawler():
    crawled_weather_data = get_weather_data(machine_read=True).splitlines()
    weather_return = Weather(
        temperature=crawled_weather_data[0],
        air_pressure=crawled_weather_data[1],
        humidity=crawled_weather_data[2],
        wind_power=crawled_weather_data[3],
        wind_direction=crawled_weather_data[4],
        velocity_ms=crawled_weather_data[5],
        velocity_kmh=crawled_weather_data[6],
    )
    return weather_return


if __name__ == '__main__':
    print(fzj_weather_crawler())
