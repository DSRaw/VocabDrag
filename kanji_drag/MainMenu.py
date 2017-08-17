'''
Created on Aug 14, 2017

@author: Daphne

This module contains the logic code for the MainMenuGUI class.

**Currently only contains code to pop up the GUIs for the deck conversion window
and the game window.
'''
#TODO: Disable multiple window at once opening. Maybe by disabling buttons
from DeckConverterGUI import DeckConverterGUI
from GameGUI import GameGUI
from TestClass import TestClass

def open_converter_window(top):
    converter_window = DeckConverterGUI(top)
    
def open_game_window(top):
    game_window = GameGUI(top)
    
def open_test_window(top):
    test_window = TestClass(top)
    test_window.add_donkey()

#settings_path    
#array = settingsvals
#def set_tick_box    #grabs setting on tick and stores in settingsvals

#def save_settings  #save in formatted txt. Save on both click of "save" and click of "play game"
    #settingsvals to txt conversion
    #global settings_path = path
    
#def on_click_run_game
    #Game.run(settings_path)