class SpellClass():
    def __init__(self, name = None, school = None, level = None, description = None) -> None:
        self.name = name
        self.school = school
        self.level = level
        self.description = description
        return
    
    def __str__(self):
        return f"{self.name}\nLevel: {self.level}\nSchool: {self.school}\nDescription: {self.description}"