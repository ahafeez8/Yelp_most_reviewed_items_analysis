'''
Place this code inside the photo dataset so it can seperate out
the needed photos as in the pair list
'''

import os
import json

copyto = "extracted"	#create this folder first

#read file 
with open("photo_rev_pairs.json", 'r',encoding='utf-8') as f:
    reviews = json.loads(f.read())

#create a list of photo ids
photo_ids = []
for i in range(len(reviews)):
        photo_ids.append(reviews[i]['photo_id'])
        
#identify photos by ids and copy them to another dir
for i in photo_ids:
	copy_command = "copy \""+i+".jpg\" \"../"+copyto+"/"+i+".jpg\"" #linux command cp
	print(copy_command)
	os.system(copy_command)
