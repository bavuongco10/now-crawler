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

delivery_ids_obj = search_delivery_ids.crawl()
delivery_ids = delivery_ids_obj['reply']['delivery_ids']

data = []

count = 0
for request_id in delivery_ids:
    detail = get_detail.crawl(request_id)
    dishes = get_delivery_dishes.crawl(request_id)
    data.append({ 'request_id': request_id, 'get_detail': detail, 'get_delivery_dishes': dishes})
    
    count += 1
    print('count:', count)
    