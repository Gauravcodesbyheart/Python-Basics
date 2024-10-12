class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy +self.chem+self.math)/3) + "%"

    def calcpercentage(self):
        self.percentage = str((self.phy+self.chem+self.math)/3) + "%"

s1 = student(98,97,99)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
s1.calcpercentage()
print(s1.percentage)


