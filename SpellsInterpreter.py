from SpellClass import SpellClass

def splitSpells(string: str) -> list:
    spells = string.split('\n \n')
    spells.pop(0)
    return spells


def getSpellsObjects(spellsArray: list) -> list:
    spellsObjectsArray = []
    for spell in spellsArray:
        if(spell == ' ' or spell == ' \n '):
            continue

        isValidSpell = __getSpellInfo(spell)
        if(isValidSpell):
            spellsObjectsArray.append(isValidSpell)
        else:
            spellsObjectsArray[-1].setSpecialDescription(adictionalDescription = spell)
            
    return spellsObjectsArray


def __getSpellInfo(spellString: str) -> SpellClass:
    infos = spellString.split('\n')
    
    for index, info in enumerate(infos):
        if(info.find('Duração :') != -1):
            headerFinalIndex = index

    if('headerFinalIndex' not in locals()):
       return False
    
    if(infos[0] == ' '):
        infos.pop(0)
        infos[0] = infos[0][1:-1]
        headerFinalIndex -= 1

    name = infos[0].lower().title().rstrip()
    spellTipeInfos = __getSpellTipeInfo(infos[1])
    castingTime = __getSpellCastingTime(infos[2])
    range = __getSpellRange(infos[3])

    componentsIndex = next((index for index, item in enumerate(infos) if "Componentes" in item), -1)
    durationIndex = next((index for index, item in enumerate(infos) if "Duração" in item), -1)

    components = __getSpellComponents(__getSpellComponentsString(infos[componentsIndex:durationIndex]))
    duration = __getSpellDuration(infos[durationIndex])
    description = ''

    for descriptionPart in infos[headerFinalIndex+1:]:
        description += descriptionPart

    spell = SpellClass(name = name,
                        school = spellTipeInfos['school'],
                          level = spellTipeInfos['level'],
                            ritual = spellTipeInfos['ritual'],
                              castingTime = castingTime,
                                range = range,
                                  verbal = components['verbal'],
                                    somatic = components['somatic'],
                                      material = components['material'],
                                        materialComponents = components['materialString'],
                                          concentration = duration['concentration'],
                                            duration = duration['duration'],
                                              description = description.rstrip())
    return spell


def __getSpellTipeInfo(string: str) -> dict :
    if(string.find('Truque') != -1):
        stringParts = string.split('de ')
        level = 0
    else:
        stringParts = string.split('nível de ')
        level = int(stringParts[0][0])

    stringParts = stringParts[1].split(' ')
    ritual = False

    if(stringParts[1].find('ritual') != -1):
        ritual = True
        
    school = stringParts[0].capitalize()
    
    return {"level": level, "school": school, "ritual": ritual}

def __getSpellCastingTime(string: str) -> str :
    return __getRawInfo(string)

def __getSpellRange(string: str) -> str :
    return __getRawInfo(string)

def __getSpellComponents(string: str) -> dict :
    componentsString = __getRawInfo(string)

    verbal = componentsString.find('V') != -1
    somatic = componentsString.find('S') != -1
    material = componentsString.find('M') != -1
    materialString = None
    if(material):
        parts = componentsString.split("(")
        materialString = parts[1]
        materialString = materialString.split(")")[0].rstrip()

    return {"verbal": verbal, "somatic": somatic, "material": material, "materialString": materialString}

def __getSpellComponentsString(infosComponents: list) -> str :
    componentsInfo = ''
    for info in infosComponents:
        componentsInfo += info

    return componentsInfo

def __getSpellDuration(string: str) -> dict :
    durationString = __getRawInfo(string)

    concentration = durationString.find('Concentração') != -1

    if(concentration):
        durationString = durationString.split("até ")[1]

    return {"concentration": concentration, "duration": durationString}

def __getRawInfo(string: str) -> str :
    stringParts = string.split(' : ')

    return stringParts[1].rstrip()