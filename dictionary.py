#Write a Python program to get the value of a specific key from a dictionary.
#Add a new key-value pair to an existing dictionary.
#Merge two dictionaries.
#Delete a key from a dictionary.
list_ed={'game':2
      ,'power':4
      ,'style':6
      ,'show':9
      }
list_va={'user':3
         ,'mobile':9
         ,'apple':2
         }
list_m=list_ed | list_va # | (Union Operator) used to merge dictionaries
print("print new listttttttttt:",list_m)

#print ("power",list_ed["power"])

list_ed["Dictionary"]=43
print("new list",list_ed)


list_m.pop('apple',2)
print("new liiiiiist:",list_m)
