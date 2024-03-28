"""
-------------------------------------------------
   File Name:    windy_api -> qweather
   Created by:   PyCharm
   Author:       linxiaxing
   date:         2024/3/28
-------------------------------------------------
   Description:
                 This file was created at 10:39:
-------------------------------------------------
"""
from typing import Literal, Union
import requests
from easydict import EasyDict


class QWeather:
    def __init__(self, config: EasyDict = None):
        self.cfg = config
        self.api_url = self._free_url_filter(config.api_url, config.is_free)
        self.geo_url = config.geo_url
        self.key = config.key
        self.data_key = config.data_key
        self.language = config.language

    def _free_url_filter(self, url, is_free) -> str:
        if is_free:
            return url.replace('api.qweather.com', 'devapi.qweather.com')
        return url

    def get_city(self, city_kw):
        url_v2 = f"{self.geo_url}lookup?" \
                  f"location={city_kw}&key={self.key}"
        city = requests.get(url_v2).json()['location'][0]

        city_id = city['id']
        district_name = city['name']
        city_name = city['adm2']
        province_name = city['adm1']
        country_name = city['country']
        lat = city['lat']
        lon = city['lon']

        return city_id, district_name, city_name, province_name, country_name, lat, lon

    def get_weather(self,
                    type: Literal["warning", "grid-weather", "weather"],
                    location: Union[int, str]
                    ) -> dict | list | None:
        url = f"{self.api_url}{type}/now?" \
               f"location={location}&lang={self.language}&key={self.key}"
        try:
            req = requests.get(url)
            if req.status_code == 200:
                return req.json()[self.data_key[type]]
            return None
        except Exception as e:
            print(f"ERROR: {e}")
            return None


