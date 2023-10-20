cakes=[
    {"id":1,"name":"blueburry","shape":["round","square","heart"],"varient":[
        {"price":3000,"weight":"1kg"},
        {"price":2800,"weight":"0.5kg"}
    ]},
    {"id":2,"name":"blackforest","shape":["round","square","heart"],"varient":[
        {"price":3500,"weight":"1kg"},
        {"price":3200,"weight":"0.5kg"}
    ]},
    {"id":3,"name":"whiteforest","shape":["round","square","heart"],"varient":[
        {"price":4800,"weight":"1.5kg"},
        {"price":3800,"weight":"1kg"}
    ]},
    {"id":4,"name":"red velvet","shape":["round","square","heart"],"varient":[
        {"price":3000,"weight":"1kg"},
        {"price":2500,"weight":"0.5kg"}
    ]},
    {"id":5,"name":"dream cake","shape":["round","square","heart"],"varient":[
        {"price":3050,"weight":"1kg"},
        {"price":2850,"weight":"0.5kg"}
    ]},
]

# print 1 kg cake price below 3500 -------
# cake_below=[c.get("name") for c in cakes for v in c.get("varient") if v.get("price")<3500 and v.get("weight")==("1kg")]
# print(cake_below)

# most costly 1 kg cake-----------
# price_one=[v.get("price")  for c in cakes for v in c.get("varient") if v.get("weight")=="1kg"]
# costly_cake=max(price_one)
# print(costly_cake)


# dream cake 1kg price
# print([v.get("price") for c in cakes for v in c.get("varient") if v.get("weight")==("1kg") and c.get("name")==("dream cake") ])

# cakes range between 3000 and 4000
# print(set([c.get("name") for c in cakes for v in c.get("varient") if v.get("price") in range(3000,4000) ]))

# print 1kg dream cake price?
print([v.get("price") for c in cakes if c.get("name")=="dream cake" for v in c.get("varient") if v.get("weight")=="1kg"])
# for c in cakes:
#     if c.get("name")=="dream cake":
#         for v in c.get("varient"):
#             if v.get("weight")=="1kg":
#                 print(v.get("price"))


