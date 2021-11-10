


import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]  
e=["Name","Designation","Age","Salary"]

a1={}
b1={}
c1={}
d1={}

emp={}


for i in range(len(a)):
    a1.update({e[i]:a[i]})
for j in range(len(b)):
    b1.update({e[j]:b[j]})
for k in range(len(c)):
    c1.update({e[k]:c[k]})
for l in range(len(d)):
    d1.update({e[l]:d[l]})

emp.update({"emp1":a1,"emp2":b1,"emp3":c1,"emp4":d1})


json_file=open("que_8_employe.1.json","w")
json.dump(emp,json_file,indent=4)



