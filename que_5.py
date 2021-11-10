# Question 5
# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?



import json
a='{"shivi":"2.2","nunu":"3+7j","shinu":3+5j,"4+3J":3.3}'
out_file = open("que_5.json", "w")
json.dump(a, out_file, indent = 6)
out_file.close()
