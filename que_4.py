# Question 4
# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho? Example:
#  Input :- Output:- JSON data:


import json

dict={'4': 5, '6': 7, '1': 3, '2': 4}

x=(json.dumps(dict,sort_keys=True))
print(x)



