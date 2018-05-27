'''
helper code:
creates a list of business names with business ids as key
for ease of access in extracting results'''

import json

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


dt1 = read_d('dataset/business.json',50000)
business = [json.loads(x) for x in dt1]

data,bnames = {},[]
for i in range(len(business)):
    data[business[i]['business_id']] = business[i]['name']


with open('bnames.json', 'w') as outfile:
    json.dump(data, outfile)
   



