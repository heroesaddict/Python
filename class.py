class Team:
    def teamName(self, name, pointguard):
        self.name=name
        self.pointguard=pointguard
    def printName(self):
        print(self.name, "pointguard is ",self.pointguard)

teampointguard=Team()
teampointguard.teamName("Brooklyn Nets", "Jeremy Lin")
teampointguard.printName()
    


class className:
    def classFunction1(instance pointer, argument1, argument2):
        argument1 pointer=argument1 container
        argument2 pointer=argument2 container
    def classFunction2(instance pointer):
        print(argument1 pointer, "pointguard is ",argument2 pointer)

instance=Team()
instance.classFunction1("Brooklyn Nets", "Jeremy Lin")
instance.classFunction2()
    
