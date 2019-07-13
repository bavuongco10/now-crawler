#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:17:04 2019

@author: user
"""

from fake_useragent import UserAgent

user_agent = UserAgent()


def generate_headers():
    return {
    'x-foody-api-version': '1',
    'Origin': 'https://www.now.vn',
    'x-foody-client-language': 'vi',
    'User-Agent': user_agent.random,
    'x-foody-client-type': '1',
    'x-foody-app-type': '1004',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'x-foody-client-id': '',
    'x-foody-access-token': '',
    'DNT': '1',
    'x-foody-client-version': '3.0.0',
}