import sys
import bst
import string
import random
import json
import util

data = bst.BST()

def test_insert_performance():
    with open("../data/material.json") as f:
        material = json.loads(f.read())

    for item in material:
        data.put(util.date_to_float(item['Master'].get('Timestamp', None)), item)

def test_get_all_keys():
    with open("../data/material_l.json", "w") as f:
        f.write(json.dumps(data.get_data_all_keys()))

def test_get_keys_ceiling():
    with open("../data/material_d.json", "w") as f:
        f.write(json.dumps(data.get_data_range_keys(data.ceiling(554980170.533),
                                                   data.get_max())))
