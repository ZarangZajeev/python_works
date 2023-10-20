from json import load
with open("D:\\MY PC\\july_python_works\\process_json\\movies\\db.json",encoding="utf-8") as movie:
    data=load(movie)
# print(len(data))

# movie_name=[mv.get("Title") for mv in data ]
# print(movie_name)

# director={d.get("Director") for d in data }
# director.discard("N/A")
# print(director)


# filter_data=[d for d in data if d.get("imdbRating")!="N/A"]
# top_movie=max(filter_data,key=lambda d:float(d.get("imdbRating")))
# print(top_movie.get("Title"))


# print all genre
# --------------------

all_genres=set()
for m in data:
    for gn in m.get("Genre").split():
        all_genres.add(gn.rstrip(","))
print(all_genres)

# print all movies with action Genre
for mv in data:
    if mv.get("Genre").count("Action")>0:
        print(mv.get("Title"))

# movies released before 2024
for mv in data:
    released_date=mv.get("Released")
    year=released_date.split(" ")[-1]
    if year.isdigit():
        if int(year)>2014:
            print(mv.get("Title"),mv.get("Released"))