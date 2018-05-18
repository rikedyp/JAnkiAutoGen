#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Automatic japanese cloze generator
# Input Japanese text and get back a massive set of cloze deletion problems
# Eventually: Get back an anki deck you can import

# TODO:
# generate cloze from text e.g.
# APIの変更に互換性のない場合はメジャーバージョンを
# =>
# API の 変更 に 互換性 の ない 場合 は メジャー バージョン を
# APIの{cloze::変更}{furigana::へんこう}に互換性のない場合はメジャーバージョンを
# + for all other non-particle words initially?
# Don't repeat for multiple instances of same word
# Add optional furigana
import MeCab
from sqlconnect import JASQL as sql
import uuid
import sys

if __name__ == "__main__":

    # --- Get text from file

    with open('sentence.txt', 'r') as file:
        data = file.read().replace('\n', '')
    t = MeCab.Tagger("-Owakati")
    s = t.parse(data)
    wordlist = s.split(" ")
    wordlist.remove("\n")
    #wordlist = set(wordlist)
    # print(data)
    # print(s)
    # print(wordlist)
    for word in wordlist:
        printstring = "*"+word+"*"
        print(printstring)

    # --- Commit to sqlite3 database
    # Connect to file in same folder
    db = sqlite3.connect('testDeck.anki2')
    # Get cursor
    cursor = db.cursor()
    # Execute sample code
    db.close()
    sql()