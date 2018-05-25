# Automatic Japanese Anki Cloze Generator
Program to generate cloze-deletion anki cards from text in 日本語

# CONTENTS
- [Overview](#overview)
- [Installation Instructions](#installation-instructions)

### Overview
Version: 0.9  
Status: Basic functionality (good for song lyrics with no punctuation)  
The Automatic Japanese Anki Cloze Generator will do what it says on the tin.  
  Method:  
  - Use python / mecab to split Japanese text into words / particles separated by " "    
  - Create cloze-deletions from text  
  - Use genanki to create an anki deck and package it as .apkg  

### Installation Instructions
Quickstart:  
 - Install dependencies:
 	- python3
 	- python3 mecab  
 		https://github.com/SamuraiT/mecab-python3  
 		pip install --user mecab-python3  
 	- python3 genanki  
 		https://github.com/kerrickstaley/genanki
 	- python3 jaconv (not sure about python 2.7)
 		pip install --user jaconv
 - Clone or download this repo
 - cd JAnkiAutogen/
 - ./JAnkiAutogen [infile(.txt)] [outfile.apkg] ["Deck Title"]  
 	Converts Japanese text in infile into cloze deletion flash cards and outputs outfile.apkg  
 	Passing no arguments takes text from input.txt and outputs TestDeck.apkg
  
 Current Anki version: 2.0.50
