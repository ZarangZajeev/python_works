data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
    ]


def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"

def retrieve(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id ]
    return obj

def get(*args,**kwargs):
    return data

print(create(id=105,name="onePlus",price=25000))

print(retrieve(id=105))
    
print(get())

    #  book