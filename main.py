#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:27:49 2019

@author: user
"""

import search_delivery_ids
import get_detail
import get_delivery_dishes
import imp

imp.reload(search_delivery_ids)
imp.reload(get_detail)
imp.reload(get_delivery_dishes)

total_delivery_ids = []


for combine_category in search_delivery_ids.combine_categories:
    payload = search_delivery_ids.default_payload
    payload['combine_categories'] = [combine_category]
    delivery_ids_obj = search_delivery_ids.crawl(payload)
    delivery_ids = delivery_ids_obj['reply']['delivery_ids']
    for id in delivery_ids:
        if(id not in total_delivery_ids): total_delivery_ids.append(id)


data = []

count = 0
for request_id in total_delivery_ids:
    detail = get_detail.crawl(request_id)
    dishes = get_delivery_dishes.crawl(request_id)
    data.append({ 'request_id': request_id, 'get_detail': detail, 'get_delivery_dishes': dishes})
    
    count += 1
    print('count:', count)
    