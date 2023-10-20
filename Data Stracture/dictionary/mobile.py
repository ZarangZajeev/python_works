mobile={"brand":"mi","display":"AMOLED","processor":"Snapdragon","price":25000,"item":"Note 12 pro"}
print(mobile["brand"])
mobile["offer"]="5%"
current_price=mobile["price"]
dicount=(current_price/100)*5
print(dicount)
mobile["Offer price"]=5000
mobile["price"]-=dicount
print(mobile["price"])
# print(mobile)
# print("display" in mobile)
# print("price" in mobile)
# print(f"Keys: {list(mobile.keys())}")
# print(f"Values: {list(mobile.values())}")
# for key, values in mobile.items():
#     print(key,values)
# print(mobile)