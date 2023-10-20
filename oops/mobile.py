class Mobiles:
    data=[
            {"id":100,"name":"galaxya5","price":35000},
            {"id":101,"name":"mi11i","price":25000},
            {"id":102,"name":"iphone15","price":135000},
            {"id":103,"name":"s23","price":145000},
            {"id":104,"name":"neo","price":35000},
        ]
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
        return f"{kwargs} Created"
    
    def get(**kwargs):
        return Mobiles.data

    def retrieve(self,id,*args,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        return obj
    
    def destroy(self,id,*args,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj} removed from data, New data is {self.data}"
    
    def put(self,id,*args,**kwargs):                    # update
        obj=[m for m in self.data if m.get("id")==id].pop()
        obj.update(kwargs)
        return f"{obj} has been updated, New data base is {self.data}"

obj=Mobiles()
print(obj.create(id=105,name="Realme GT",Price=23999))

print(Mobiles.get())

print(obj.retrieve(id=103))

print(obj.destroy(id=102))

print(obj.put(id=104,name="Realme Neo"))



# list all mobiles
# print details of a specific mobiles
# update mobile
# delete a mobile
# list, retrieve, edit,delete
    
# crud  c=> creat, r=>read, u=>update, d=>delete

