class Team:
    def teamName(self, name, pointguard):
        self.name=name
        self.pointguard=pointguard
    def printName(self):
        print(self.name, "pointguard is ",self.pointguard)

teampointguard=Team()
teampointguard.teamName("Brooklyn Nets", "Jeremy Lin")
teampointguard.printName()
    
