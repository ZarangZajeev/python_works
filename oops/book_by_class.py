# class Book:
#     data=[
#             {"book_no":1001,"name":"Wing of Fire","Author":"APJ Abdul Kalam","Publisher":"DC","Price":500},
#             {"book_no":1002,"name":"The Cricket on the Hearth","Author":"Charles Dickens","Publisher":"ABC","Price":400},
#             {"book_no":1003,"name":"The Daffodil Sky","Author":"H. E. Bates","Publisher":"DC","Price":450},
#             {"book_no":1004,"name":"Behold the Man","Author":"Michael Moorcock","Publisher":"DC","Price":900},
#             {"book_no":1005,"name":"No Highway","Author":"Nevil Shute","Publisher":"BN Books","Price":900},
#             {"book_no":1006,"name":"A Time of Gifts","Author":"Patrick Leigh Fermor","Publisher":"MNKV","Price":550},
#             {"book_no":1007,"name":"Vanity Fair","Author":"William Makepeace Thackeray","Publisher":"American Books","Price":1005},
#         ]
#     def create(self,*args,**kwargs):
#         self.data.append(kwargs)
#         return f"{kwargs} Successfully created"
    
#     def retrieve(self,book_no,*args,**kwargs):
#         obj=[b for b in self.data if b.get("book_no")==book_no].pop()
#         return obj
    
#     def get(*args,**kwargs):
#         return Book.data
    
#     def destroy(self,book_no,*args,**kwargs):
#         obj=[b for b in self.data if b.get("book_no")==book_no].pop()
#         self.data.remove(obj)
#         return f"{obj} removed from data base, New data base id {self.data}"

#     def put(self,book_no,*args,**kwargs):                                   # update
#         obj=[b for b in self.data if b.get("book_no")==book_no].pop()
#         obj.update(kwargs)
#         return f"{obj} hes been updated, New data base is {self.data}"
    
# obj=Book()
# print(obj.create(book_no="1008",name="Aadu Jeevitham",Author="Vaikom Muhhammed Basheer",Publisher="DC Books",Price=775))

# print(obj.retrieve(book_no=1004))

# print(obj.get())

# print(obj.destroy(book_no=1003))

# print(obj.put(book_no=1006,Price=1750))

