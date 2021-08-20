# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2021/8/20 10:05
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
# -*- encoding: utf-8 -*-

from fastapi import FastAPI


app = FastAPI()




@app.get("/getOne")
def get_product():

    return True
