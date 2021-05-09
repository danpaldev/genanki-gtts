About genanki

genanki is amazing, but its documentation is mostly crap. Because of this, I could never find
how to add the mediafiles in a dynamic or efficient way using genanki api.

So, the best way to do it manually is to just generate your decks as it they contain media
(reference the media in the fields), and after the deck generation just put the media files
(with the exact name that you used for filling the field in the script) in the collections.media folder
of your anki installation.

---------------------


main.py

This file basically helps to generate TTS files on mp3 of russian and english words
contained inside a CSV.

These audios will be the ones that you have to manually put inside the collections.media
folder.