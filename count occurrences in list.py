#Count occurrences of a specific element in a list.
list_occurrence=['nam','class','name','address','game','class','name']
count=1
for i in list_occurrence:
    if i =='name':
        count+=1
    else: 
        continue
print ("name=",count)

#Output: name=3