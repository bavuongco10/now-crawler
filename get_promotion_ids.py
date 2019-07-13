#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:11:59 2019

@author: user
"""


import requests
from header_utils import generate_headers

headers = generate_headers()

default_payload = {"city_id":217,"foody_service_id":1,"sort_type":0,"promotion_status":1}


def crawl(payload=default_payload):
    print('Begin get promotion ids:')
    response = requests.post('https://gappapi.deliverynow.vn/api/promotion/get_ids', headers=headers, json=payload)
    result_json = response.json()
    print('End get promotion ids:')
    return result_json

