# Question 7
# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai? Example: Input :- Output:-

# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29




# import json
# with open("example.txt","w") as file:
#     json.dump(file,indent=4)





import json


# the file to be converted to
# json format
filename = 'example.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename) as fn:

	for line in fn:

		# reads each line and trims of extra the spaces
		# and gives only the valid words
		command, description = line.strip().split(None, 1)

		dict1[command] = description.strip()

# creating json file
# the JSON file is named as test1
out_file = open("que_7.test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()


