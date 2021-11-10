import json

my_dict={
    "place":"pune",
    "wather":"normal",
    "study":"in navgurukul",
    "trinking":"water"
}




x=open("dump.json","w")
json.dump(my_dict,x,indent=4)



