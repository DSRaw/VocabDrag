'''
Created on Jul 29, 2017

@author: Daphne
'''

import Tkinter
import ttk
import re

#Internal modules:
from MainMenuGUI import MainMenuGUI
from GameGUI import GameGUI
from DeckConverterGUI import DeckConverterGUI


if __name__ == '__main__':
    root = Tkinter.Tk()
    main_window = MainMenuGUI(root) #creates and displays the main menu that should be the first thing shown upon program start
    #Currently, DeckConverterGUI is hard-coded to open alongside with kanji_main. This can be prevented by commenting out the following line
    
    
    
    #Game Mode flags:
    #eng_drag: If False: Kanji will be in dragFrame. If True: English will be in dragFrame
    #reading_drag: if None: reading will not be shown. If False, kana will be shown in dropFrame. If True: kana will be shown in dragFrame
    #the "reading" should be the kana reading of the corresponding kanji.
    eng_drag = False                                                             
    reading_drag = None
    start_position = 0      #where in deck to begin set
    practice_set_size = 0   #number of cards practiced at a time
    
    #example data:
    start_position = 1
    practice_set_size = 5
    reading_drag = False

    root.mainloop()