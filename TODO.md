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
- 1.0 Make linux / windows / (mac maybe) executables  
	pyinstaller
- 1.0 .deb installer
- .dmg / apple mac
- .rpm / other installers (platform independent?)
- 1.0 Consistent use of "", ''
- 1.0 Implement options  
	- Kanji words only
	- Nouns only
	- Furigana on/off)
- Think of ways to try and break it 
	- 2.0 Options for multiple readings
			Use NKF?
		鳥達
		いたる should be toritachi but not really a word (song lyrics)
		止ん
		とまん should be yanda
		芳しい kanbashii / kaguwashii 
		multiple readings should appear as option input (CLI) or popup (GUI)
	- Non japanese text - 
- Put setup instructions into README
	- 1.0 Make sure setup instructions are comprehensive

### CLI
In built command line interface for linux
- 1.0 Put it in the docs

### GUI
- Create GUI in PyQt (kivy has IME input issues) OR Tkinter
	- Paste text directly
	- Select file containing text

### Licensing
- 1.0 Determine which license / notice files need to be included in the project (e.g. MIT)
	- python
	- MeCab
	- genanki
  	- Qt / PyQt
