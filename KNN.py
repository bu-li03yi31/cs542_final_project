import csv
import pandas as pd
import numpy as np
import json
from collections import defaultdict

#load file
user_item_df = pd.read_csv("user_item.txt")
user_item_df.columns = ['index','user', 'item']
user_item_df.drop('index', axis=1, inplace=True)

#group by user and get the total vote of each user
tmp = user_item_df.groupby(['user']).count()
user_votes = []
for index, item in tmp.iterrows():
    c = int(item['item'])
    tp = [index, c]
    user_votes.append(tp)

#save results to another dataframe
user_votes_df = pd.DataFrame(user_votes)
user_votes_df.columns = ['user','count']

#print the mean of votes per user
print user_votes_df['count'].mean()
#print number of users in trainning set
print len(user_votes_df)

import math
from collections import OrderedDict
from operator import itemgetter
import csv
import pandas as pd
import numpy as np
import json
from collections import defaultdict
    
def prediction(user_a, item_j, compare_users_data, alpha):
    tmp = {}
    for user_i in compare_users_data:
        _list = compare_users_data[user_i]
        if user_a is not user_i and len(_list) > alpha:
            v_ij = 0
            if item_j in _list:
                v_ij = 1
            w = getWeight2(user_a, user_i, compare_users_data)
            tmp[user_i] = w
    
    sorted_tmp = sorted(tmp.iteritems(), key=itemgetter(1), reverse=True)
    nearest_neighbour = [sorted_tmp[0][0], sorted_tmp[1][0],sorted_tmp[2][0],sorted_tmp[3][0],sorted_tmp[4][0],sorted_tmp[5][0],sorted_tmp[6][0],sorted_tmp[7][0],sorted_tmp[8][0]]
    
    W = 0
    total = 0
    big_list = []
    for user in nearest_neighbour:
        _list = compare_users_data[user]
        big_list = big_list + _list
    if item_j in list(set(big_list)):
        return 1
    else:
        return 0


import json
import math

def getWeight(a, i, compare_users_data):
    set1 = set(compare_users_data[a])
    set2 = set(compare_users_data[i])
    length1 = len(set1)
    length2 = len(set2)
    inter = set1.intersection(set2)
    den1 = math.sqrt(length1)
    den2 = math.sqrt(length2)
    res = float(len(inter)) / (den1 * den2)
    return res

def getWeight2(a, i, compare_users_data):
    set1 = set(compare_users_data[a])
    set2 = set(compare_users_data[i])
    union = set1.union(set2)
    inter = set1.intersection(set2)
    res = float(len(inter)) / len(union)
    return res

with open('user_item_dict.json') as data_file:    
    compare_users_data = json.load(data_file)

print prediction("10077","1004",compare_users_data,4)

def KNNTest(alpha):
    f_file = "user_item_test.txt"
    total = 0
    count = 0
    for l in open(f_file):
        if l.startswith(","):
            continue
        a = l.split(",")
        user = a[1]
        item = a[2].rstrip('\n')
        total = total + 1
        res = prediction(user, item,compare_users_data,alpha)
        if res == 1:
            count = count + 1
        
    return float(count) / total

print 'Alpha is 4: '
print KNNTest(4)
print '\n'

print 'Alpha is 6: '
print KNNTest(6)
print '\n'

print 'Alpha is 9: '
print KNNTest(9)
print '\n'
