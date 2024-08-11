import PyPDF2
import os
from SpellClass import SpellClass

os.system('cls')

""" ESTUDAR """
def visitorBody(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50:
        parts.append(text)

def removeDoubleSpaces(string):
    string = string.replace('  ', ' ')
    return string

def splitSpells(string):
    spells = string.split('\n \n')
    spells.pop(0)
    return spells

def getSpellsObjects(spellsArray):
    spellsObjectsArray = []
    for spell in spellsArray:
        spellsObjectsArray.append(getSpellInfo(spell))
    
    return spellsObjectsArray

def getSpellInfo(spellString):
    infos = spellString.split('\n')
    
    for index, info in enumerate(infos):
        if(info.find('Duração :') > -1):
            headerFinalIndex = index

    name = infos[0]
    level = int(infos[1][0])
    school = infos[1].split('nível de ')[1].capitalize()
    description = ''

    for descriptionPart in infos[headerFinalIndex+1:]:
        description += descriptionPart

    spell = SpellClass(name, school, level, description)
    return spell
        

pdfFile = open('players_handbook_ptbr.pdf', 'rb')

pdf = PyPDF2.PdfReader(pdfFile)

parts = []

spellsString = ''

for page in [pdf.pages[213], pdf.pages[215]]:
    page.extract_text(visitor_text=visitorBody)
    spellsString += "".join(parts)

spellsString = removeDoubleSpaces(spellsString)

spellsArray = splitSpells(spellsString)
""" print(repr(spellsString)) """
""" for spell in spellsArray:
    print(spell)
    print("===============================================") """

spells = getSpellsObjects(spellsArray)

for spell in spells:
    print(spell)
    print("\n") 