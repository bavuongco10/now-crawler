#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:16:40 2019

@author: user
"""

import json
from os import path


def write(data, file_name, file_folder='result/json'):
	file_path = path.join(file_folder, file_name) + '.json'
	output_file = open(file_path, 'w')
	json.dump(data, output_file, ensure_ascii=False)
	output_file.flush()
	print(f'Saved {file_path}')
	return file_path