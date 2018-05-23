#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Automatic japanese cloze generator
# Input Japanese text and get back a massive set of cloze deletion problems
# Eventually: Get back an anki deck you can import

# TODO:
#   - Make it work for single sentence
#       - Make it function and write the docs
#   - Make it work for a paragraph
#   - Make it work for several paragraphs (e.g. song lyrics)
#   - Make it work for a large document (e.g. wikipedia article or https://semver.org/lang/ja/)
#       - Auto split into paragraphs (would anyone paste a whole document like this?)
#   - Make it easy to choose:
#       - Add new notes to existing deck
#       - Create brand new deck

# METHOD:
# Deck GUIDs from random.randrange(1 << 30, 1 << 31)
# generate cloze from text e.g.
# APIの変更に互換性のない場合はメジャーバージョンを
# =>
# API の 変更 に 互換性 の ない 場合 は メジャー バージョン を
# APIの{cloze::変更}{furigana::へんこう}に互換性のない場合はメジャーバージョンを
# + for all other non-particle words initially?
# Don't repeat for multiple instances of same word
# Add optional furigana
import MeCab
import genanki
import re
import random
import sys

def get_id():
    newid = random.randrange(1 << 30, 1 << 31)
    return newid

def create_note(cloze, sentence, model):
    # TODO: sentence -> paragraph / wholetext
    note = genanki.Note(
        model=model,
        fields=[cloze, sentence],
        sort_field = '',
        tags = None,
        guid = random.randrange(1 << 30, 1 << 31),
        )
    return note

def create_deck(clozes, sentence, deckfile = 'JAnkiAutogen_Output.apkg', setname = "Default Deck"):
    # Create anki deck from words / text block
    # TODO: Can we retrieve / load an existing deck / deck ID?
            # Need to pass sentence
    # Access / generate deck
    newid = get_id()
    deck = genanki.Deck(newid, setname)
    # Set up card model
    model = genanki.Model(
        1607392319,
        'Word',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{Answer}}'
            }]
    )
    # Generate notes (flashcards)
    for cloze in clozes:
        clozenote = create_note(cloze, sentence, model)
        deck.add_note(clozenote)
    #deck.add_note(note)

    genanki.Package(deck).write_to_file(deckfile)

def load_text(textfile):
    with open(textfile, "r") as file:
        text = file.read()#.replace("\n", " ") # Might need modifying for paragraphs / documents
        #text = unicode(text, 'utf-8')
    t = MeCab.Tagger("-Owakati")
    s = t.parse(text)
    # Convert to unicode
    s = unicode(s, 'utf-8')
    text = unicode(text, 'utf-8')
    wordlist = s.split(" ")
    wordlist.remove("\n")
    # TODO: Remove punctuation e.g. "。"
    # TODO: Check for sentences with multiple instances of same word
    return text, wordlist

def rejig_text(sentence, wordlist):
    #print(wordlist)
    clozes = []
    #print(sentence)
    for word in wordlist:
        cloze = re.sub(word, '[...]', sentence)
        #cloze = cloze.decode('utf-8')
        clozes.append(cloze)
    return clozes

if __name__ == "__main__":

    # IDEA: Return GUID on first run which user can hard-code in / save per deck in a library?
    # --- Get text from file
    # TODO Choose a text file when you run it:
    #   $python main.py filename.txt
    #   Eventually: $JAnkiAutogen infile.txt outfile.apkg
    sentence, wordlist = load_text('input.txt') # os.path | argument in terminal | look for default filename?
    #sentence = unicode(sentence, 'utf-8')
    # --- Turn text into clozes for printing to screen
    clozes = rejig_text(sentence, wordlist)
    print(sentence)
    # put html <br /> line breaks for Anki
    sentence = sentence.replace('\n', '<br />')
    clozes = rejig_text(sentence, wordlist)
    # Create anki deck from cloze deletions
    create_deck(clozes, sentence, 'TestDeck.apkg', 'JAA Test Deck')
    print("Deck built.")