'''
Created on Aug 14, 2017

@author: Daphne
'''
import Tkinter
import ttk

import MainMenu


class MainMenuGUI(object):
    '''
    This is the main menu of the Vocab GrabBag game that will allow the use to:
    customize the options for their game,
    start the game (create the GameGUI window),
    and convert their deck for use with the game (create the DeckConverterGUI window)
    '''


    def __init__(self, root):
        '''
        **This is currently just test code that makes it easier to view only the 
        windows relevant for editing/testing at any given time
        '''
        self.main_menu = root
        self.main_menu.title("Vocab GrabBag")
        self.main_menu.minsize(width="256", height="144")               #a minimum 16:9 aspect ratio I chose based on personal preference
        
        #Passing the toplevel window from here to children GUI classes necessitates using a lambda
        self.convert_button = ttk.Button(self.main_menu, text="Add a Deck", command=lambda: MainMenu.open_converter_window(self.main_menu))
        self.convert_button.pack()
        
        self.play_button = ttk.Button(self.main_menu, text="Play Vocab GrabBag", command=lambda: MainMenu.open_game_window(self.main_menu))
        self.play_button.pack()
        
        self.test_button = ttk.Button(self.main_menu, text="Test Window", command=lambda: MainMenu.open_test_window(self.main_menu))
        self.test_button.pack()