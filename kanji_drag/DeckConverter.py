'''
Created on Aug 13, 2017

@author: Daphne

This module contains the logic code that DeckConverterGUI depends on.
It contains the functions called by events in the deck_converter_GUI window.
These functions facilitate the conversion of a deck into a format usable by
the kanjiDrag game.
'''

import collections          #an ordered dictionary is essential to ease of displaying card fields in correct order
import random               #needed to randomly pick a card from the deck to display as an example
import re                   #regex is needed to split fields in file by tab delimiter
import tkFileDialog         #for browsing for a file

#TODO: replace global objects with get() and set() conventions
curObj = None           #will hold the current instance of the DeckConverter GUI
old_deck = []


'''
The following group of functions are called from DeckConverter and primarily
facilitate the functionality of widgets that utilize events and callbacks
'''
#the following function passes the current relevant instance of the DeckConverterGUI window to this module
def set_instance(obj):
    global curObj
    curObj = obj
    
#the following function should allow the user to browse their file system for a deck file. Triggered when the browse button in this GUI is clicked
def browse_filesystem():
    global old_deck                                                             #Necessary to update deck_path outside this function
    
    deck_path = tkFileDialog.askopenfilename(filetypes=[("Text", "*.txt")])
    
    try:
        old_deck = _init_origin_deck(deck_path)
        _roll_and_display(old_deck)
    except IOError, e:
        if e.errno == 22:
            print "File not selected, or path invalid."
    
#The following function will select another random card from the deck and update the data to display the example data from this new card
def re_roll():
    if old_deck:
        _roll_and_display(old_deck)

#The following function should create a new deck from the old deck that includes only the fields the user chose to keep from the old deck
def convert_deck():
    #ask where to save deck as a file
    global curObj
    global old_deck
    new_deck = []
    
    keys = _get_choices()
    
    if len(keys) > 2:                                                           #The user should select at least 2 fields
        for card in old_deck:   #possibly replaceable by enumerate
            new_card = collections.OrderedDict()   #see if there is a function that auto copies key:value pairs from one dict to another
            for key in keys:
                new_card[key] = card[key]
            new_deck.append(new_card)
        
        print new_deck[42].values()[0]
        print new_deck[42].values()[1]
        #print new_deck[42].values()[2]
        _update_runFrame()
    else: print "You must select at least 2 fields" #TODO: replace with popup error message
       
'''
The following group of functions are called internally within this module and
serve as the logic that facilitates the display and conversion of the deck
'''  

#The following function will reset to GUI to be ready for a new conversions session
def _reset_GUI():
        print
#The following function will display a message indicating completion of conversion and button to allow user to run another conversion
def _update_runFrame():
    curObj.rerunButton.pack(fill="both", expand="1")
    curObj.runLabel.pack(fill="both", expand="1")   #displays message indicating completion of conversion
    
#The following function will handle rolling for a random example card and displaying the example data
def _roll_and_display(deck):
    sample = _get_random_card(old_deck)
    _populate_exampleFrame(sample)
    _populate_chooseFrame(sample)

#The following function should load all cards in the original, unconverted deck into an array of dicts
def _init_origin_deck(path):
    deck_list = []
    
    deck = open(path,"r")
    lines = deck.readlines()
    deck.close()

    #potential use-case for enumerate?
    for line in lines:                                                          #for each line in the deck,
        card_dict = collections.OrderedDict()                                   #instantiate an empty ordered dict
        words = re.split(r'\t+', line)                                          #split the words in the line, and
        field = 1
        for word in words:                                                      
            card_dict["Field {}".format(field)] = word                          #add them as key:value pairs to the dict
            field+=1
        deck_list.append(card_dict)                                             #then add the current line's dict to the deck array
     
    return deck_list

#The following function should pick a random card from the deck and return a dict of all its fields
def _get_random_card(deck):
    return random.choice(deck)

#The following function will show the randomly selected card as an example in the GUI's cardFrame
def _populate_exampleFrame(card):
    global curObj
    line = ""
    
    for key in card.keys():
        line += "{}    {}\n".format(key, card[key])                             #Stores each key:value text in a single string
     
    curObj.exampleCanvas.itemconfig(curObj.textID, text=(line))                 #sets the text in the cardFrame canvas to that string
    curObj.exampleCanvas.config(scrollregion=curObj.exampleCanvas.bbox("all"))  #Sets the scroll region to encompass the string
    #print line
    
#The following function inserts list of all fields of the card into the comboboxes for the user to choose from
def _populate_chooseFrame(card):
    global curObj   
    curObj.vocabCombobox.configure(values=card.keys())
    curObj.transCombobox.configure(values=card.keys())
    curObj.pronunCombobox.configure(values=card.keys())
    
#The following function gets which fields the user chose in the combo box once the convert button is pressed
def _get_choices():
    global curObj
    keys = []
    
    keys.append(curObj.vocabCombobox.get())
    keys.append(curObj.transCombobox.get())
    keys.append(curObj.pronunCombobox.get())
    
    #The following accounts for a user not selecting a value
    for key in keys:
        if key == "":
            keys.remove(key)
        
    return keys
