class SpellClass():
    def __init__(self, name = None, school = None, level = None, ritual = None, description = None, specialDescription = False) -> None:
        self.name = name
        self.school = school
        self.level = level
        self.ritual = ritual
        self.description = description
        self.specialDescription = specialDescription
        return
    
    def __str__(self):
        return f"{self.name}\nLevel: {self.level}\nSchool: {self.school}\nRitual: {self.ritual}\nDescription: {self.description}"
    
    def setSpecialDescription(self, adictionalDescription):
        self.specialDescription = True
        newDescriptionPiece = ''
        
        for descriptionPart in adictionalDescription.split('\n'):
            newDescriptionPiece += descriptionPart

        self.description += '\n\n' + newDescriptionPiece