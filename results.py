import numpy
import json
from itertools import groupby
import pickle

#tags contains results with accuracy > 70%
file = open('tags.txt', 'rb')
# dump information to that file
data = pickle.load(file)


with open("photo_rev_pairs.json", 'r',encoding='utf-8') as f:
    pr = json.loads(f.read())
with open("bnames.json", 'r',encoding='utf-8') as f:
    bnames = json.loads(f.read())

#generating results 
for i in range(len(pr)):
    pid = pr[i]['photo_id']
    for j in range(len(data)):
        if pid in data[j][2] and data[j][0] != 'plate':
            if pr[i]['stars'] >= 4: #threshholding
                print(bnames[pr[i]['business_id']],'has ',data[j][0],'as most positively reviewed item')
            if pr[i]['stars'] < 4:
                print(bnames[pr[i]['business_id']],'has ',data[j][0],'that did not get good reviews')

