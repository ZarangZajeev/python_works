from json import load
with open("D:\MY PC\july_python_works\process_json\products\item.json",encoding="utf-8") as shop:
    data=load(shop)

# total number of products?
# ------------------
# print(len(data))



# print all categorie?
# ------------------
# all_category={c.get("category") for c in data }
# print(all_category)




# print electronic product names ?
# ---------------------------
# electronic_items=[ep.get("title") for ep in data if ep.get("category")=="electronics"]
# print(electronic_items)
# >>>>>>>>
# for ep in data:
#     if(ep.get("category")=="electronics"):
#         print(ep.get("title"))




# top rated product ?
# -----------------
top_rated=max(data,key=lambda tr:float(tr.get("rating").get("rate")))
# print(top_rated.get("title"))




# product having women's clothing price range(100-300)?
# --------------------------------
womens_cloth=[wcp.get("title") for wcp in data if wcp.get("category")=="women's clothing" and wcp.get("price")>20 and wcp.get("price")<=30]
# print(womens_cloth)



# which product got most number of rating ?

t_rate=max(data,key=lambda rate:float(rate.get("rating").get("count")))
# print(t_rate.get("title"))



# jwellery product with rating >3
# ------------------------

rate_greater=[ra.get("title") for ra in data if ra.get("category")=="jewelery" if ra.get("rating").get("rate")>3]
# print(rate_greater)



# sort product with price order bt decending order?
# -------------------------------
srt_items=sorted(data,reverse=True,key=lambda p:p.get("price"))
# for p in srt_items:
    # print(p.get("title"))
# print(srt_items)


# category wise product count?
# ---------------------------
wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
print(wc)

val_key=[(v,k) for k,v in wc.items()]
print(max(val_key))
print(max(val_key,key=lambda lst:lst[0]))