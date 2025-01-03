<h1>Helloo. Welcome to DnDSpellsReader!</h1>

<h2>Introduction</h2>

It's a small project I'm doing to get the spells from D&D 5e Players Handbook and put then into a database. The idea came when I was playing D&D and I found it very difficult to search for the spells in the book. So, I decided to create a whole system that saves the spells in a database that can be used by an API later. <br/>
I'm seizing this oportunity to learn more about Python and some different libraries as [PyPDF2](https://pypi.org/project/PyPDF2/) and [google-generativeai](https://pypi.org/project/google-generativeai/).<br/>
For now, it's available only for the PTBR version of Players Handbook. Maybe I'll add other languages in the future.

<h2>Install</h2>

Install Python 3.12 <br/>

Create a venv (default name "venv")<br/>
`py -m venv venv`
<br/>

Install PyPDF2 <br/>
`pip install PyPDF2`
<br/>

Install python-dotenv<br/>
`pip install python-dotenv`
<br/>

Install google-generativeai<br/>
`pip install google-generativeai`
<br/>


Paste the PDF of D&D 5e Players Handbook PTBR version in main folder (default name "players_handbook_ptbr.pdf")
<br/>

Create .env file and put your Gemini API key in the `GEMINI_API_KEY` variable (only if you want to use AI text improvement using `-ai` parameter)