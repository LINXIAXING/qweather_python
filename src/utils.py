"""
-------------------------------------------------
   File Name:    windy_api -> utils
   Created by:   PyCharm
   Author:       linxiaxing
   date:         2024/3/28
-------------------------------------------------
   Description:
                 This file was created at 14:06:
-------------------------------------------------
"""
import json
import os
from typing import Union


def save_dict(data: Union[dict, list], filename: str):
    datas = [data] if isinstance(data, dict) else data
    if not os.path.isdir("./datas"):
        os.mkdir("./datas")
    filepath = os.path.join("./datas", filename)
    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            datas.extend(json.loads(f.read()))
    with open(filepath, "w+", encoding="utf-8") as f:
        f.write(json.dumps(datas, ensure_ascii=False, indent=4))