from SpellClass import SpellClass

def splitSpells(string):
    spells = string.split('\n \n')
    spells.pop(0)
    return spells


def getSpellsObjects(spellsArray):
    spellsObjectsArray = []
    for spell in spellsArray:
        spellsObjectsArray.append(__getSpellInfo(spell))
    
    return spellsObjectsArray


def __getSpellInfo(spellString):
    infos = spellString.split('\n')
    
    for index, info in enumerate(infos):
        if(info.find('Duração :') > -1):
            headerFinalIndex = index

    """ for a in infos:
        print(a)
    print('\n') """
    name = infos[0].lower().title()
    spellTipeInfos = __getSpellTipeInfo(infos[1]) 
    description = ''

    for descriptionPart in infos[headerFinalIndex+1:]:
        description += descriptionPart

    spell = SpellClass(name, spellTipeInfos['school'], spellTipeInfos['level'], spellTipeInfos['ritual'], description)
    return spell

def __getSpellTipeInfo(spellTipeString):
    stringParts = spellTipeString.split('nível de ')
    level = int(stringParts[0][0])
    stringParts = stringParts[1].split(' ')
    ritual = False

    if stringParts[1].find('ritual') != -1:
        ritual = True
        
    school = stringParts[0].capitalize()
    
    return {"level": level, "school": school, "ritual": ritual}