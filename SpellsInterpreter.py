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

    if(infos[0] == ' '):
        infos.pop(0)
        infos[0] = infos[0][1:-1]
    
    for index, info in enumerate(infos):
        splitedInfo = __getRawInfo(info)
        if(splitedInfo == False):
            continue

        if(__verifyWordsCompatibility('Tempo de Conjuração', splitedInfo['firstString'])):
            castingTimeIndex = index
            continue
        if(__verifyWordsCompatibility('Alcance', splitedInfo['firstString'])):
            rangeIndex = index
            continue
        if(__verifyWordsCompatibility('Componentes', splitedInfo['firstString'])):
            componentsIndex = index
            continue
        if(__verifyWordsCompatibility('Duração', splitedInfo['firstString'])):
            durationIndex = index
            headerFinalIndex = index
            continue

    if('headerFinalIndex' not in locals()):
       return False
    
    if('rangeIndex' not in locals()):
       index = infos[castingTimeIndex].find('Alcance')
       if(index != -1):
           infos.insert(castingTimeIndex+1, infos[castingTimeIndex][index:])
           infos[castingTimeIndex] = infos[castingTimeIndex][:index]
           rangeIndex = castingTimeIndex+1
           componentsIndex = componentsIndex+1
           durationIndex = durationIndex+1
           headerFinalIndex = headerFinalIndex+1
           
    
    name = infos[0].lower().title().rstrip()
    spellTipeInfos = __getSpellTipeInfo(infos[1])
    castingTime = __getSpellCastingTime(infos[castingTimeIndex:rangeIndex])

    if('componentsIndex' not in locals()):
        range = __getSpellRange(infos[rangeIndex:durationIndex])
        components = {"verbal": False, "somatic": False, "material": False, "materialString": None}
    else:
        range = __getSpellRange(infos[rangeIndex:componentsIndex])
        components = __getSpellComponents(__getSpellInfoString(infos[componentsIndex:durationIndex]))

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

def __getSpellCastingTime(infos: list) -> str :
    return __getRawInfo(__getSpellInfoString(infos))['secondString']

def __getSpellRange(infos: list) -> str :
    return __getRawInfo(__getSpellInfoString(infos))['secondString']

def __getSpellComponents(string: str) -> dict :
    componentsString = __getRawInfo(string)['secondString']

    verbal = componentsString.find('V') != -1
    somatic = componentsString.find('S') != -1
    material = componentsString.find('M') != -1
    materialString = None
    if(material):
        parts = componentsString.split("(")
        materialString = parts[1]
        materialString = materialString.split(")")[0].rstrip().capitalize()

    return {"verbal": verbal, "somatic": somatic, "material": material, "materialString": materialString}

def __getSpellInfoString(infos: list) -> str :
    infoString = ''
    for info in infos:
        infoString += info

    return infoString

def __getSpellDuration(string: str) -> dict :
    durationString = __getRawInfo(string)['secondString']

    concentration = durationString.find('Concentração') != -1

    if(concentration):
        durationString = durationString.split("até ")[1]

    return {"concentration": concentration, "duration": durationString}
    

def __getRawInfo(string: str) -> dict :
    if(string.find(': ') == -1):
        return False
    stringParts = string.split(': ')
   
    return {"firstString": stringParts[0].rstrip(), "secondString": stringParts[1].rstrip()}

def __verifyWordsCompatibility(baseString: str, stringToVerify: str):
    for i in range(len(stringToVerify)):
        try:
            if(i > len(baseString)-1 and i > len(stringToVerify)-1):
                continue
            if(stringToVerify[i] == baseString[i]):
                continue

            if(stringToVerify[i] == ' ' and stringToVerify[i+1] == baseString[i]):
                stringToVerify = stringToVerify[:i] + stringToVerify[i+1:]
        except:
            return False

    return stringToVerify == baseString