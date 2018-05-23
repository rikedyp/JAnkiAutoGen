# TODO
Place all TODOs in here
There may be todos inside any .py or .kv files
- 0.1 target version for this TODO
- Can you contribute to any of the projects this planner uses to help them and us run smoother and/or on more devices?
  - Python
  - MeCab / Python-MeCab
  - Qt / PyQt

### CONTENTS
- [General](#general)
- [CLI](#cli)
- [GUI](#gui)
- [Licensing](#licensing)

### General
- Consider using Github stuff instead of big long TODO files?
- Test how to break this:
	- English / non japanese text?

- ISSUE: Seem to be getting duplicate cards sometimes
- Consider using included font (check licensing / permissions)
- 1.0 Have a file selection function
- 1.0 Test what happens if you:
	- Create a new deck new name
	- Create second deck second name
	- Run the program with first deck file name
		- Are new notes just added to first deck again or does guid matter?
- Put setup instructions into README
	- 1.0 Make sure setup instructions are comprehensive
		- I think genanki was modified
- 1.0 Error catching!
- 1.0 Optional Auto-Furigana
	- Get furigana from MeCab (check mepytest.py)
	- Incorporate to anki decks (test python-generated anki decks for furigana (how does Anki do it?))
- Consider beautifying flash cards  
	https://www.reddit.com/r/LearnJapanese/comments/37ddh7/any_way_to_make_flashcard_fonts_bigger_in_anki/

### CLI
In built command line interface for python
	- Paste text?
	- Choose a file?
	- What's the point?
- Put it in the docs

### GUI
- Create GUI in PyQt (kivy has IME input issues) OR Tkinter
	- Paste text directly
	- Select file containing text

### Licensing
- Determine which license / notice files need to be included in the project (e.g. MIT)
	- python
	- MeCab
	- genanki
  	- Qt / PyQt
