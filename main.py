import csv
from os import path
from retrying import retry
from gtts import gTTS

f = open('ruswords.csv', newline='', encoding="utf-8")
reader = csv.reader(f)
#Skipping rows on csv file - https://stackoverflow.com/a/40404006/13954598
for skip in range(948):
    next(reader)

def script(reader):
    for row in reader:
        word = row[0].split("(")[0].split("/у-")[0].split("/о-")[0].split("/по-")[0].split("/за-")[0].split("/с-")[0]
        wordForFile = word.split("/")[0]  # because files can't have slashes
        eng_text = row[1]
        if path.isfile("ru" + wordForFile + ".mp3"):  # to not run over the same word twice
            pass
        else:
            save_word(word, wordForFile)
            savetext_eng(eng_text, wordForFile)
        # pass


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

f.close()