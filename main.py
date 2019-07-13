#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:27:49 2019

@author: user
"""

import search_delivery_ids
import get_detail
import get_delivery_dishes
import get_promotion_ids
import write_json
import imp

imp.reload(search_delivery_ids)
imp.reload(get_detail)
imp.reload(get_delivery_dishes)
imp.reload(get_promotion_ids)

total_delivery_ids = []

def append_unique(final_array, added_array):
    for item in added_array:
        if(item not in final_array): final_array.append(item)

for combine_category in search_delivery_ids.combine_categories:
    payload = search_delivery_ids.default_payload
    payload['combine_categories'] = [combine_category]
    delivery_ids_obj = search_delivery_ids.crawl(payload)
    delivery_ids = delivery_ids_obj['reply']['delivery_ids']
    append_unique(total_delivery_ids, delivery_ids)


promotion_ids_obj = get_promotion_ids.crawl()
promotion_ids = promotion_ids_obj['reply']['promotion_ids']
append_unique(total_delivery_ids, promotion_ids)

print('Total request ids:', len(total_delivery_ids))

data = []

count = 0
for request_id in total_delivery_ids:
    detail = get_detail.crawl(request_id)
    dishes = get_delivery_dishes.crawl(request_id)
    
    request_data = { 'request_id': request_id, 'get_detail': detail, 'get_delivery_dishes': dishes}
    json_name = f'request_id-{request_id}'
    write_json.write(data, json_name)
    data.append(request_data)
    
    count += 1
    print('count:', count)
    