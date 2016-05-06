#import packages
#Collaborator: Yiteng Xu, Changlei Shi, ChenCheng Wang, Yi Li
import csv
import pandas as pd
import numpy as np
import json
from collections import defaultdict

#define a file reader for future use
def readJson(f):
    for l in open(f):
        yield eval(l)

#split anonymous-msweb.data into item.txt (item table)
#and user_item.txt (user-item relation table)
items = []
for l in open("anonymous-msweb.data"):
    if l.startswith("A"):
        m,n,p,q,i = l.strip().split(',')
        q = q[1:-1]
        i = i[1:-1]
        tmp = [n, q, i]
        items.append(tmp)

items_df = pd.DataFrame(items)
items_df.to_csv("item.txt")

current = ""
item = ""
user_item = []
training_user_item_dict = {}

for l in open("anonymous-msweb.data"):
    if l.startswith("C"):
        m,n,p = l.strip().split(',')
        current = p
    if l.startswith("V"):
        a,b,c = l.strip().split(',')
        item = b
        tp = [current, item]
        user_item.append(tp)
        if current in training_user_item_dict:
            cur_list = training_user_item_dict[current]
            cur_list.append(item)
            training_user_item_dict[current] = cur_list
        else:
            my_list = [item]
            training_user_item_dict[current] = my_list
user_item_df = pd.DataFrame(user_item)
user_item_df.to_csv("user_item.txt")

json_str = json.dumps(training_user_item_dict)
data = json.loads(json_str)
with open('user_item_dict.json', 'w') as f:
    json.dump(data, f)

import json
items = []

for l in open("anonymous-msweb.test"):
    if l.startswith("A"):
        m,n,p,q,i = l.strip().split(',')
        q = q[1:-1]
        i = i[1:-1]
        tmp = [n, q, i]
        items.append(tmp)

items_df = pd.DataFrame(items)
items_df.to_csv("item_test.txt")

current = ""
item = ""
user_item = []
training_user_item_dict = {}
for l in open("anonymous-msweb.test"):
    if l.startswith("C"):
        m,n,p = l.strip().split(',')
        current = p
    if l.startswith("V"):
        a,b,c = l.strip().split(',')
        item = b
        tp = [current, item]
        user_item.append(tp)
        if current in training_user_item_dict:
            cur_list = training_user_item_dict[current]
            cur_list.append(item)
            training_user_item_dict[current] = cur_list
        else:
            my_list = [item]
            training_user_item_dict[current] = my_list
user_item_df = pd.DataFrame(user_item)
user_item_df.to_csv("user_item_test.txt")

#print training_user_item_dict
json_str = json.dumps(training_user_item_dict)
data = json.loads(json_str)
with open('user_item_dict_test.json', 'w') as f:
    json.dump(data, f)
