import PyPDF2
import os
import SpellsInterpreter

os.system('cls')

""" ESTUDAR """
def visitorBody(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50:
        parts.append(text)

def removeDoubleSpaces(string):
    string = string.replace('  ', ' ')
    return string

pdfFile = open('players_handbook_ptbr.pdf', 'rb')

pdf = PyPDF2.PdfReader(pdfFile)
spellsPages = pdf.pages[213:289]

parts = []

spellsString = ''

for page in spellsPages:
    page.extract_text(visitor_text=visitorBody)

spellsString += "".join(parts)
spellsString = removeDoubleSpaces(spellsString)

spellsArray = SpellsInterpreter.splitSpells(spellsString)

spells = SpellsInterpreter.getSpellsObjects(spellsArray)

for spell in spells:
    print(spell)
    print("------------------")
    print("\n")