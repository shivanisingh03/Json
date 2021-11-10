# Question 2
# Q.2 Python object ko json data main convert karne ka program likho?





import json
dict={
    "Name":"Ram",
    "Class":"IV", 
    "Age":9
}

out_file = open("que_2.json", "w")
json.dump(dict, out_file, indent = 6)
out_file.close()









