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

def create_note(word, sentence, model):
    # TODO: sentence -> paragraph / wholetext
    note = genanki.Note(
        model=model,
        fields=['This sentence is a [...] deletion', 'This sentence is a <b>cloze</b> deletion'],
        sort_field = '',
        tags = None,
        guid = random.randrange(1 << 30, 1 << 31),
        )
    return note

def create_deck(sentence, wordlist, deckfile = 'JAnkiAutogen_Output.apkg', setname = "Default Deck"):
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
    for word in wordlist:
        note = create_note(word, sentence, model)
        #deck.add_note(note)
    deck.add_note(note)

    genanki.Package(deck).write_to_file(deckfile)

def load_text(textfile):
    with open(textfile, "r") as file:
        text = file.read().replace("\n", " ") # Might need modifying for paragraphs / documents
    t = MeCab.Tagger("-Owakati")
    s = t.parse(text)
    wordlist = s.split(" ")
    wordlist.remove("\n")
    # TODO: Remove punctuation e.g. "。"
    # TODO: Check for sentences with multiple instances of same word
    return text, wordlist

def rejig_text(sentence, wordlist):
    sentences = []
    #print(sentence)
    for word in wordlist:
        cloze = re.sub(word, '[...]', sentence)
        print(cloze)
    # wordlist = text.split(" ")
    # print(wordlist)
    # wordlist = set(wordlist)
    # for word in wordlist:
    #     print(word)
    #     cloze = re.sub(r'\b'+word+r'\b', '[...]', text)
    #     sentences.append(cloze)
    # return sentences

if __name__ == "__main__":

    # --- Get text from file
    sentence, wordlist = load_text('sentence.txt') # os.path | argument in terminal | look for default filename?
    sentences = rejig_text(sentence, wordlist)
    #print(sentences)