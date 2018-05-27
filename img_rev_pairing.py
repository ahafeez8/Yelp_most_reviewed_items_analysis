'''
Following code generates image review pairs:
no direct link exist between reviews and attached photos,
so jaccard similarity between image caption and review is taken
to find related pairs'''

import json
import pickle
import re, math
from collections import Counter
import numpy as np
import re
from nltk.corpus import stopwords
from itertools import groupby

class Similarity():
#jaccard similarity takes intersection of pairs
    def jaccard_similarity(self, string1, string2):
        intersection = set(string1).intersection(set(string2))
        union = set(string1).union(set(string2))
        return len(intersection)/float(len(union))
    
#for opening rest of dataset = individual records
def read_d(filename,chunkSize):
    data = []
    x =0
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if (x == chunkSize):
                break
            data.append(line)
            x +=1
    return data
#loading data
dt1 = read_d('dataset/review.json',50000)
reviews = [json.loads(x) for x in dt1]

dt2 = read_d('dataset/photos.json',50000)
photos = [json.loads(x) for x in dt2]

#extract intermidiatory data 
pbid,pcap, count = [],[],[]
bp,new_pid = {}, []
for j in range(len(photos)):
    pbid.append(photos[j]['business_id'])
    pcap.append((photos[j]['business_id'], photos[j]['caption'], photos[j]['photo_id']))

#group photos based on business ids
for key, group in groupby(pcap, lambda x: x[0]):
    new_photos = []
    for thing in group:
        new_photos.append((thing[1],thing[2])) #pairs of set of captions and photo id
    bp[key] = new_photos

#create instance of similarity
similarity = Similarity()

new_bid,pairs = [],[]
keep_rev = []


for i in range(len(reviews)):
    bid = reviews[i]['business_id']
    if bid in pbid:  
        keep_rev.append(reviews[i]) #extracting reviews containing photos
        for j in range(len(bp[bid])):
            jaccard = similarity.jaccard_similarity(reviews[i]['text'],bp[bid][j][0]) #find similarity of review against set of captions
            jaccard *=100
            jaccard = int(round(jaccard))
            if(jaccard >= 60): #similarity threshhold
                x = {'photo_id':bp[bid][j][1],'review_id':reviews[i]['review_id'],'stars':reviews[i]['stars'], 'business_id':reviews[i]['business_id']}
                pairs.append(x)

print(len(pairs)) #about 4k
#save pairs in file later                 
with open('photo_rev_pairs.json', 'w') as outfile:
    json.dump(pairs, outfile) #write pairs to a file to use later
   





