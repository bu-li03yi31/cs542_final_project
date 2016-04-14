#import packages
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
for l in open("anonymous-msweb.data"):
    if l.startswith("C"):
        m,n,p = l.strip().split(',')
        current = p
    if l.startswith("V"):
        a,b,c = l.strip().split(',')
        item = b
        tp = [current, item]
        user_item.append(tp)
    
user_item_df = pd.DataFrame(user_item)
user_item_df.to_csv("user_item.txt")
