class emp:
    id=1
    name="abc"
    def display(self):
        print(self.id)
        print(self.name)

#STEP 1
e=emp()

#STEP 2
e.display()


# ACCESS THE CLASS
class ashutosh:
    id=432
    fullname="asuhtosh sunil patil"
    edu="BE Mech"
    age=23
    def sports(self):
        print("Chess,200 metre sprinter,handball,cricket")
    def food(self):
        print("few items of NORTH INDIAN,all items of South indian only")
    def singers(self):
        print("arigit singh,shreya ghoshal")

# STEP 1
a=ashutosh()

#STEP 2
print(a.id)
print(a.fullname)
print(a.edu)

a.sports()
a.food()
a.singers()