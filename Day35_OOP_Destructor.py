class  baby:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print("Hello World")
        print(self.id)
        print(self.name)




    def __del__(self):
        print("Baby information is deleted")

b=baby(1,"Arya")

del b



