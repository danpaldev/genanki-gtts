import genanki
import random
import csv
from os import path
from retrying import retry
from gtts import gTTS

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
            'qfmt': '{{English}}{{English_Audio}}',
            'afmt': '{{FrontSide}}{{Russian}}{{Russian_Audio}}{{Index}}{{Example}}'
        }
    ])

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
        if counter > 5:
            break
        else:
            counter = counter + 1
            print(counter)
            word = row[0].split("(")[0].split("/у-")[0].split("/о-")[0].split("/по-")[0].split("/за-")[0].split("/с-")[0]
            wordForFile = word.split("/")[0]  # because files can't have slashes
            eng_text = row[1]
            if path.isfile("ru/" + wordForFile + ".mp3"):  # to not run over the same word twice
                print(f'[sound:{wordForFile}.mp3]')
                my_note = genanki.Note(
                    model=my_model,
                    fields=[wordForFile, eng_text, f'[sound:{wordForFile}.mp3]', f'[sound:{wordForFile}_eng.mp3]', row[2], str(counter)]
                )
                my_deck.add_note(my_note)
            else:
                pass



@retry(wait_exponential_multiplier=1000, wait_exponential_max=40000)
def save_word(word, wordForFile):
    print(word)
    tts = gTTS(word, lang="ru")
    # Speech.save(Speech(word, "RU"), + wordForFile + ".mp3")
    tts.save( "ru/" + wordForFile + ".mp3")


@retry(wait_exponential_multiplier=1000, wait_exponential_max=40000)
def savetext_eng(eng_text, wordForFile):
    print(wordForFile + "_eng")
    tts = gTTS(eng_text)
    # Speech.save(Speech(word, "RU"), + wordForFile + ".mp3")
    tts.save( "eng/" + wordForFile + ".mp3")

script(reader)

genanki.Package(my_deck).write_to_file('testengru.apkg')

f.close()

