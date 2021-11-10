# Question 8
# Q8.Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai 
# jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary 
# honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke 
# aapko ek json file create karni hai? Jaise ki niche diya hai. Output:-

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


employee={"emp1":a1,"emp2":b1,"emp3":c1,"emp4":d1}

for i in range(len(a)):
    a1.update({e[i]:a[i]})
for j in range(len(b)):
    b1.update({e[j]:b[j]})
for k in range(len(c)):
    c1.update({e[k]:c[k]})
for l in range(len(d)):
    d1.update({e[l]:d[l]})

json_=open("que_8_employe.json","w")
json.dump(employee,json_,indent=4)












