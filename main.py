import PyPDF2
import os
import SpellsInterpreter
import time
import dotenv
import argparse
from GeminiAiClass import GeminiAiClass

os.system('cls')
dotenv.load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument('-ai', action='store_true', help='Utilizar melhoria de texto por IA')
args = parser.parse_args()

def visitorBody(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50:
        parts.append(text)

def removeDoubleSpaces(string: str) -> str:
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

if(args.ai):
    geminiAi = GeminiAiClass(os.environ['GEMINI_API_KEY'])

    for spell in spells:
        spell.name = geminiAi.correctText(spell.name)
        time.sleep(5)
        spell.description = geminiAi.correctText(spell.description)
        time.sleep(5)

    geminiAi.finish()

for spell in spells:
    print(spell)
    print("------------------")
    print("\n")

print("=========== It's over ===========")