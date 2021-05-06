from google_speech import Speech
import csv
from os import path
from retrying import retry
# from gtts import gTTS

f = open('ruswords.csv', newline='', encoding="utf-8")
reader = csv.reader(f)


def script(reader):
    for row in reader:
        word = row[0].split("(")[0].split("/у-")[0].split("/о-")[0].split("/по-")[0].split("/за-")[0].split("/с-")[0]
        wordForFile = word.split("/")[0]  # because files can't have slashes
        if path.isfile(wordForFile + ".mp3"):  # to not run over the same word twice
            pass
        else:
            save_word(word, wordForFile)
        # pass


@retry(wait_exponential_multiplier=1000, wait_exponential_max=40000)
def save_word(word, wordForFile):
    print(word)
    Speech.save(Speech(word, "RU"), + wordForFile + ".mp3")


# print("hello aaaa bbbb cccc".split(" ")[0])

script(reader)

f.close()
