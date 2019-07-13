# -*- coding: utf-8 -*-

import requests
from header_utils import generate_headers

headers = generate_headers()

def generate_params(request_id):
    return (
            ('id_type', '2'),
            ('request_id', request_id),
            )



def crawl(request_id):
    print('Begin get delivery dishes:',request_id)
    params = generate_params(request_id)
    response = requests.get('https://gappapi.deliverynow.vn/api/dish/get_delivery_dishes', headers=headers, params=params)
    result_json = response.json()
    print('End get delivery dishes:',request_id)
    return result_json