frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

# for fw in frameworks:
#     print(fw.get("name"))
#     print(fw.get("rating"))
# fw_name=[fw.get("name") for fw in frameworks]
# print(fw_name)

# fw_rating=[fw.get("rating")for fw in frameworks]
# print(fw_rating)

# fw_python=[for fw in frameworks val]
# for fw in frameworks:
#     if fw.get("language")=="python":
#         print(fw.get("name"))

python_fw=[fw.get("name") for fw in frameworks if fw.get("language")=="python" ]
print(python_fw)


rating_fw=[fw.get("name") for fw in frameworks if fw.get("rating")==5]
print(rating_fw)


id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4) ]
print(id_filter)

lower_rating=min(frameworks, key=lambda fw: fw.get("rating"))
print(lower_rating)

top_rating=max(frameworks, key=lambda fw: fw.get("rating"))
print(top_rating)