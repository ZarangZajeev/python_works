from json import load
path="D:\MY PC\july_python_works\process_json\countries\data.json"
with open(path,encoding="utf-8") as f:
    data=load(f)
print(len(data))
print()

# all regions????????????
all_regions={r.get("region") for r in data }
print(all_regions)
print()


# Asian region countries???????????
asian_countries=[a.get("name") for a in data if a.get("region")=="Asia" ]
print(asian_countries)
print()

# independent countries??????????????
independent_countries=[i.get("name") for i in data if i.get("independent")==True ]
print(independent_countries)
print()


# name name of country with highest population???????????????
population=max(data,key=lambda p:p.get("population"))
print(population.get("name"))
print()


# indian border sharing countries???????????????????????
indian_borders=[b.get("borders") for b in data if b.get("name")=="India" ]
print(indian_borders)