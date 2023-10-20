data=[
    {"book_no":1001,"name":"Wing of Fire","Author":"APJ Abdul Kalam","Publisher":"DC","Price":500},
    {"book_no":1002,"name":"The Cricket on the Hearth","Author":"Charles Dickens","Publisher":"ABC","Price":400},
    {"book_no":1003,"name":"The Daffodil Sky","Author":"H. E. Bates","Publisher":"DC","Price":450},
    {"book_no":1004,"name":"Behold the Man","Author":"Michael Moorcock","Publisher":"DC","Price":900},
    {"book_no":1005,"name":"No Highway","Author":"Nevil Shute","Publisher":"BN Books","Price":900},
    {"book_no":1006,"name":"A Time of Gifts","Author":"Patrick Leigh Fermor","Publisher":"MNKV","Price":550},
    {"book_no":1007,"name":"Vanity Fair","Author":"William Makepeace Thackeray","Publisher":"American Books","Price":1005},
]

def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"

def retrieve(*args,**kwargs):
    id=kwargs.get("book_no")
    obj=[book for book in data if book.get("book_no")==id].pop() # [0]
    return obj

def get(*args,**kwargs):
    return data

def destroy(*args,**kwargs):
    id=kwargs.get("book_no")
    obj=[b for b in data if b.get("book_no")==id].pop() # [0]
    data.remove(obj)
    return f"{obj} removed from data, New Data is {data}"

def put(book_no,*args,**kwargs):                # update
    obj=[b for b in data if b.get("book_no")==book_no].pop()
    obj.update(kwargs)
    return f"{obj} has been updated, New data base is {data}"


# print(create(book_no=1008,name="The Wives of Bath",Author="Susan Swan",Publisher="American Books",Price=1450))

# print(retrieve(book_no=1006))

# print(get())

# print(destroy(book_no=1001))

# print(put(book_no=1003,name=""))

# print(put(book_no=1004,name="Today's world",Price=750))

# do with class