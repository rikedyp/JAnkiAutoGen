#!/usr/bin/env python
# -*- coding: utf-8 -*-

# genanki-test.py
# Seeing whether or not to include genanki dependency and/or source code (check licensing)
import genanki

def create_deck(deckfile):
    name = "JA Test Deck"
    deck = genanki.Deck(2059406110, 'TEST DECK NAME')
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
                'afmt': '<b>{{FrontSide}}</b>: {{Answer}}'
            }]
    )
    
    note = genanki.Note(
        model=model,
        #1160258597,
        fields=['firstbit', 'answecard'],
        sort_field = '',
        tags = None,
        guid = 1160258597,
        )
    deck.add_note(note)

    genanki.Package(deck).write_to_file(deckfile)
    
    
if __name__ == '__main__':
    create_deck('testDeck.apkg')