#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:11:59 2019

@author: user
"""


import requests
from header_utils import generate_headers

headers = generate_headers()

combine_categories = [{"code":1,"id":1},{"code":1,"id":4},{"code":1,"id":8},{"code":1,"id":16},{"code":1,"id":17},{"code":1,"id":21},{"code":1,"id":22},{"code":1,"id":30},{"code":1,"id":34},{"code":1,"id":4},{"code":1,"id":17},{"code":1,"id":9},{"code":1,"id":18},{"code":1,"id":20},{"code":1,"id":36},{"code":1,"id":38},{"code":1,"id":39},{"code":1,"id":42},{"code":1,"id":43},{"code":1,"id":44},{"code":1,"id":45},{"code":1,"id":49},{"code":1,"id":51},{"code":1,"id":52},{"code":1,"id":54},{"code":1,"id":79}]

default_payload = {
        "category_group":1,
        "city_id":217,
        "keyword":"",
        "sort_type":8,
        "foody_services":[1],
        "delivery_only": True,
        "combine_categories":[{"code":1,"id":1}]
        }


def crawl(payload=default_payload):
    print('Begin search delivery ids:', payload['combine_categories'])
    response = requests.post('https://gappapi.deliverynow.vn/api/delivery/search_delivery_ids', headers=headers, json=payload)
    result_json = response.json()
    print('End search delivery ids:', payload['combine_categories'])
    return result_json

