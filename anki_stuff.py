import genanki
import random
import csv
from os import path
from retrying import retry
from gtts import gTTS

my_css = """
.card{
font-family: consolas;
font-size: 35px;
text-align: center;
color: black;
background-color: white;
}
"""


my_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'Double Audio Model',
    fields=[
        {"name": "Russian"},
        {"name": "English"},
        {"name": "Russian_Audio"},
        {"name": "English_Audio"},
        {"name": "Example"},
        {"name": "Index"},
    ],
    templates=[
        {
            "name": "eng-rus",
            'qfmt': '{{English}}<br>{{English_Audio}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Russian}}<br>{{Russian_Audio}}<br><br>Frequency Index: {{Index}}<br><br>{{Example}}'
        }
    ],
    css=my_css
)

my_deck = genanki.Deck(
    random.randrange(1 << 30, 1 << 31),
    'eng-rus-10k')


f = open('ruswords.csv', newline='', encoding="utf-8")
reader = csv.reader(f)
#Skipping rows on csv file - https://stackoverflow.com/a/40404006/13954598
#for skip in range(1936):
#    next(reader)

counter = 0
def script(reader):
    global counter
    for row in reader:
        word = row[0].split("(")[0].split("/у-")[0].split("/о-")[0].split("/по-")[0].split("/за-")[0].split("/с-")[0]
        wordForFile = word.split("/")[0]  # because files can't have slashes
        eng_text = row[1]
        if path.isfile("ru/" + wordForFile + ".mp3"):
            counter = counter + 1
            my_note = genanki.Note(
                model=my_model,
                fields=[wordForFile, eng_text, f'[sound:{wordForFile}.mp3]', f'[sound:{wordForFile}_eng.mp3]', row[2], str(counter)]
            )
            my_deck.add_note(my_note)
        else:
            pass

script(reader)
genanki.Package(my_deck).write_to_file('eng-ru10k.apkg')

f.close()

