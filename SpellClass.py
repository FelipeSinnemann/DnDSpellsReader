class SpellClass():
    def __init__(self, name: str = None, school: str = None, level: int = None, ritual: bool = None, description: str = None, specialDescription: bool = False) -> None:
        self.name = name
        self.school = school
        self.level = level
        self.ritual = ritual
        self.description = description
        self.specialDescription = specialDescription
    
    def __str__(self) -> str:
        return f"{self.name}\nLevel: {self.level}\nSchool: {self.school}\nRitual: {self.ritual}\nDescription: {self.description}"
    
    def setSpecialDescription(self, adictionalDescription: str) -> None:
        self.specialDescription = True
        newDescriptionPiece = ''
        
        for descriptionPart in adictionalDescription.split('\n'):
            newDescriptionPiece += descriptionPart

        self.description += '\n\n' + newDescriptionPiece