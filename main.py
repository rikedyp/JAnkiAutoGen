#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Automatic japanese cloze generator
# Input Japanese text and get back a massive set of cloze deletion problems
# Eventually: Get back an anki deck you can import


import MeCab
import sys
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.lang import Builder

Builder.load_string('''
<Home>:
	on_parent: root.init()
	orientation: 'vertical'
	FileChooserListView:
		id: filechooser
		show_hidden: True
	Button:
		font_name:"DroidSansJapanese.ttf"
		text: "load file"
		on_press: root.load_file()
	TextInput:
		id: textinput
		font_name:"DroidSansJapanese.ttf"
		size_hint_y: 0.9
	BoxLayout:
		orientation: 'horizontal'
		Button:
			size_hint_y: 0.1
			text: "Create cloze"
			on_press: root.start()
	''')

class Home(BoxLayout):
	mc = MeCab.Tagger("-Owakati")
	text = "太郎はこの本を読んだ。"
	def init(self):
		# use this instead of faffing around with super
		self.ids.textinput.text = self.text
	def load_file(self, filechooser):
		self.load(filechooser.path, filechooser.selection)
	def load(self, path, selection):
		print(path, selection)
	def start(self):
		file = open("sentence.txt")
		print(file)
	def reset(self):
		self.ids.textinput.text = self.text

class AKCGApp(App):
	def build(self):
		return Home()

if __name__ == "__main__":
	print("Starting AJCG")
	AKCGApp().run()