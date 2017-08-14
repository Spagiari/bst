import sys
import bst
import string
import random
import json
import util

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def test_randon_string():
    assert(id_generator(size = 60) != None)

def test_nooby():
    data = bst.BST()
    data.put(1,"A")
    data.put(2,"B")

    for k  in data.get_all_keys():
        print (k, data.get(k))

    assert(data.check())

def test_randon_insert():
    data = bst.BST()

    for i in range(0, 100):
        data.put(random.randint(0, sys.maxsize), id_generator(size = 60))

    assert(data.check())

def test_insert_inverse():
    data = bst.BST()
    keys = [10, 9, 8, 7 ,6, 5, 4, 3, 2, 1, 0]
    for i in keys:
        data.put(i, str(i))

    j = 0
    for i in data.get_all_keys():
        assert(i == keys[10 - j])
        j += 1

def test_insert():
    data = bst.BST()
    keys = [0, 1, 2, 3, 4, 5 ,6 ,7 , 8, 9, 10]
    for i in keys:
        data.put(i, str(i))

    j = 0
    for i in data.get_all_keys():
        assert(i == keys[j])
        j += 1
