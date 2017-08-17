'''
Created on Aug 13, 2017

@author: Daphne

This module contains the logic code that DeckConverterGUI depends on.
It contains the functions called by events in the deck_converter_GUI window.
These functions facilitate the conversion of a deck into a format usable by
the kanjiDrag game.
'''


import tkFileDialog

deck_path = ""       #Test value to show this variable is accessible by multiple function in this module and is updated after browse_filesystem() runs.

file_selected = False   #

#the following function should allow the user to browse their file system for a deck file. Triggered when the browse button in this GUI is clicked
def browse_filesystem():
    global deck_path                                                            #Necessary to update deck_path outside this function
    deck_path = tkFileDialog.askopenfilename(filetypes=[("Text", "*.txt")])
    deck = open(deck_path)
    line = deck.readline()
    line2 = deck.readline()
    _populate_dataFrame(line, line2)
    deck.close()
    
def convert_deck():
    dict = {}
    
    if(deck_path != ""):                                                        #If user did not press "Cancel" on file browser
        deck = open(deck_path)
        line = deck.readline()
        print(line.split()[0].decode("utf-8"))                                                  #Test code, currently only prints filepath to console.
        deck.close()
    #TODO: An os independent solution to selecting and opening a file

def _populate_dataFrame(sample, sample2):
    card = []                                                                   #initializes array which will contain a single array that will store array of the sample data
    fields = []                                                                 #initializes array which will contain each word from the sample line
    data = sample.split()                                                       #splits each word in sample line into list of individual elements
    for word in data:
        fields.append(word)                                                     #adds each word from sample data into an element of fields array
    card.append(fields)                                                         #adds array of words from data into single element of card array
    print (card[0][0])
    
def test_func():
    return "hello"
#The following function takes control of the "X" (close) button click event of the DeckConverterGUI window
#This function will not only close the window, but will also ensure that the selected file stored in deck_path
#is no longer selected after window is closed        
def close_convert_session(root):
    global deck_path                                                   
    deck_path=""
    root.destroy()