'''
Created on Aug 15, 2017

@author: Daphne
'''

import Tkinter
import ttk
import DeckConverterGUI
import DeckConverter

class TestClass(object):
    '''
    This class was created for the purpose of testing data parsing logic,
    GUI display of data, and communication between classes and functions.
    Could potentially later be refactored relatively painlessly into Game
    module that serves as the underlying engine of the game logic
    '''


    def __init__(self, root):
        '''
        This class contains both GUI and function code
        '''
        
        self.window = Tkinter.Toplevel(root)
        
        #*NOTE:CURRENTLY IRRELEVANT -The following frame arrangement allows easy viewing of geometry comparable to that of the GameGUI
        self.containerFrame = ttk.Frame(self.window)    #topmost frame containing all children widgets
        self.containerFrame.pack()
        
        #self commenting variable names are hard. Let's pin the tail on the donkey
        self.donkeyFrame = ttk.Frame(self.containerFrame)
        self.donkeyFrame.pack()
        
        self.tailFrame = ttk.Frame(self.containerFrame)
        self.tailFrame.pack()
        
        self.donkeyLabels = []
    def add_donkey(self):    #add "frame" as variable
        deck = open("C:\Users\Daphne\My Documents\LiClipse Workspace\KanjiDrag\Rainy Genki I+II Notes.txt")
        line = deck.readline()
        text = line.split()[0].decode("utf-8")                                                  #Test code, currently only prints filepath to console.
        deck.close()
        
        self.donkeyLabel = ttk.Label(self.donkeyFrame, text=text)
        self.donkeyLabels.append(self.donkeyLabel)
        self.donkeyLabels[0].pack()
        
    #def run(settings path):
        #settings = open(settings_path)
        #deck = settings.deck_path
        #config1 = various bools for setting options
        
        