mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":650000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":450000},
    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},
    ]},
]

# all_mobiles=[mob.get("name") for mob in mobiles ]
# print(all_mobiles)

# all_brand=[mob.get("brand") for mob in mobiles]
# print(set(all_brand))

# mobile names available in 20k-40k
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,40001):
#             print(mob.get("name"))

# list conprehension--
price_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,40001) ]
print(price_filter)


# 4 gb ram
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

# list conprehension--
# ram_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")==("4gb") ]
# print(ram_filter)

# 8gb ram price < 40000

# ram_price=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")==("8gb") and v.get("price")<40001 ]
# print(ram_price)

# print(set([mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")==("8gb") and v.get("price")<40001 ]))

costly_mob=[v.get("price") for mob in mobiles for v in mob.get("varients")]
costley_price=max(costly_mob)
print(costley_price)