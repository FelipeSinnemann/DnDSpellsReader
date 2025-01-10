class SpellClass():
    def __init__(self, name: str = None, school: str = None, level: int = None, ritual: bool = None, castingTime: str = None, range: str = None, verbal: bool = False, somatic: bool = False, material: bool = False, materialComponents: str = None, concentration: bool = False, duration: str = None, description: str = None, specialDescription: bool = False) -> None:
        self.name = name
        self.school = school
        self.level = level
        self.ritual = ritual
        self.castingTime = castingTime
        self.range = range
        self.verbal = verbal
        self.somatic = somatic
        self.material = material
        self.materialComponents = materialComponents
        self.concentration = concentration
        self.duration = duration
        self.description = description
        self.specialDescription = specialDescription
    
    def __str__(self) -> str:
        return f"{self.name}\nLevel: {self.level}\nSchool: {self.school}\nRitual: {self.ritual}\nCasting time: {self.castingTime}\nRange: {self.range}\nDuration: {self.duration}\nDescription: {self.description}"
    
    def setSpecialDescription(self, adictionalDescription: str) -> None:
        self.specialDescription = True
        newDescriptionPiece = ''
        
        for descriptionPart in adictionalDescription.split('\n'):
            newDescriptionPiece += descriptionPart

        self.description += '\n\n' + newDescriptionPiece