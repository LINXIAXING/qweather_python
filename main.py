"""
-------------------------------------------------
   File Name:    windy_api -> main.py
   Created by:   PyCharm
   Author:       linxiaxing
   date:         2024/3/27
-------------------------------------------------
   Description:
                 This file was created at 09:57:
-------------------------------------------------
"""
import yaml
from easydict import EasyDict

from src.qweather import QWeather
from src.utils import save_dict


def test_qweather():
    config = EasyDict(yaml.load(open("./config.yml", "r", encoding="utf-8"), Loader=yaml.SafeLoader))
    qweather = QWeather(config.qweather)
    weather = qweather.get_weather(type="weather", location="116.41,39.92")
    warning = qweather.get_weather(type="warning", location="116.41,39.92")
    save_dict(weather, "./weather.json")
    save_dict(warning, "./warning.json")


if __name__ == '__main__':
    test_qweather()
