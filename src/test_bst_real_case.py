import sys
import bst
import string
import random
import json
import util

data = bst.BST()

def test_insert():
    with open("../data/zip.json") as f:
        zips = json.loads(f.read())

    for item in zips:
        zips[item].pop('Files')
        data.put(util.date_to_float(zips[item]['Master'].get('Timestamp',
                                                              None)),
                 zips[item])

def test_timestamp_conversion():
    maxk = data.get_max()

    ts = data.get(maxk)['Master']['Timestamp']
    fts = util.date_to_float(ts)
    nts = util.float_to_date(fts)

    assert(ts == nts)
