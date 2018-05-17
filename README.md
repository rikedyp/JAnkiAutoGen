# Automatic Japanese Anki Cloze Generator
Program to generate cloze-deletion anki cards from [paragraphs]
[sentences] of text in 日本語

# CONTENTS
- [Overview](#overview)
- [Installation Instructions](#installation-instructions)

### Overview
Version: 0.1
Status: Early development  
The Automatic Japanese Anki Cloze Generator will do what it says on the tin.
  Project plan
  - Use python / mecab to split Japanese text into words / particles separated by " "  
  - Generate anki cloze deletion cards {cloze::word} for each word in the text  
    - Avoid making multiple cards for multiple instances of word in text (one card per word)
    - Initially: generate text output which can be pasted into anki desktop app
    - Ideally: automatically generate anki deck / card files from input

### Installation Instructions
Quickstart:  
 - None
