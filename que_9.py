# Question 9
# Q.9 Apki pass ek shopping name ki ek dictionary hai Apki dictionary ka use kar ke ek json file create karna hai. Aur apko kuch task perform karne hai jaise ki 1. main dekhna chahta hu shopping list ko json file dekhna.
# 2.phir main user se poochu ga ki kon sa item khareedna chahte ho.
# 3.uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# 4.phir aapka wo number of items json file se remove karna hai.
# 5.Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.

import json
dict22={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

open_file=open("que_9.shpping.json","w")
json.dump(dict22,open_file,indent=4)

a=input("enter what you want to buy:  ")
b=int(input("how many items you want to buy:   "))

for key in dict22:
    for value in dict22:
        for i,j in dict22[key].items():
            if i==a:
                k=int(j)-b
                print("remaining items",k)


