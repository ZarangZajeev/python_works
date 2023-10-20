class Book:
    name:str
    author:str
    price:float
    publisher:str

    def set_book(self,name,author,price,publisher):
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher

    def display(self):
        print(self.name,self.author,self.price,self.publisher)

    def __str__(self): # object (string representation of objects)
        return self.name

book1=Book()
book1.set_book("Wings of fire","APJ",500,"DC books")
book1.display()
print(book1)