# SUPER KEYWORD USE

class sbi:
    def interest(self):
        print(" SBI Summer interest is 10%")

class boi(sbi):
    def interest(self):
        super().interest()
        print(" BOI Winter interest is 25%")

class hdfc(sbi):
    def interest(self):
        super().interest()
        print(" HDFC Winter interest is 15%")        

h=hdfc()    
b=boi()
b.interest()
h.interest()
# EXAMPE 2===========================================Another way of writing super keyword

class amazon:
    name="Cloths"
    def offer(self):
        print("Summer discount is 10%")

class flipcart(amazon):
    name="I phone 15 pro max"
    def offer(self):
        print(self.name)
        print(super().name)

f=flipcart()
f.offer()     
