'''
Created on Aug 6, 2017

@author: Daphne
'''
import Tkinter
import ttk

import DeckConverter 
#TODO: import DeckConverter as DC for brevity. Update button commands accordingly
 
class DeckConverterGUI(object):
    '''
    This class contains the GUI that allows options for converting an exported
    Anki deck file into a format usable with the "Kanji Drag" program.
    It will display the information collected from the deck and allow the user
    to choose what fields to include in the conversion.
    '''
    
    
    #Below is the GUI framework for DeckConverter's window      
    def __init__(self, master):                                                 #root should be root window of the main window of the GUI
        
        #The following function will populate the data in the dataFrame while also setting the value of the textvariable used in the combo boxes.
        #this will not be called until after browse_filesystem has run a deck file to be used for the data has been selected:
        
                   
        self.deckConverterRoot = Tkinter.Toplevel(master)                       #Makes DeckConverter window a separate window linked to the main GUI
        self.deckConverterRoot.title("Convert a Deck")
        self.deckConverterRoot.resizable("true","true")                         #might set this to false later to make this a fixed-width window.
        self.deckConverterRoot.minsize(width="640", height="360")               #a minimum 16:9 aspect ratio I chose based on personal preference
        
        #The following function call ensures that chosen deck file is no longer selected after window close. This takes control of "X" (close) button functionality
        self.deckConverterRoot.protocol("WM_DELETE_WINDOW", lambda: (DeckConverter.close_convert_session(self.deckConverterRoot)))
         
        #containerFrame is the outermost frame of deck_converter_root window. Contains all other frames
        self.containerFrame = ttk.Frame(self.deckConverterRoot)
        self.containerFrame.pack(fill="both", expand="1")
        
        #browseFrame is thin frame at top of this window containing the option to browse from a file
        self.browseFrame = ttk.Frame(self.containerFrame)
        self.browseFrame.pack(fill="x")
        self.browseLabel = ttk.Label(self.browseFrame, text="Select your deck:")
        self.browseLabel.pack(side="left")
        self.browseButton = ttk.Button(self.browseFrame, text="browse", command=DeckConverter.browse_filesystem)   #on click, triggers browseFileSystem function
        self.browseButton.pack(side="left")
        
        #dataFrame will contain the two frames that display an example card of the deck and allow a user to select data from it
        self.dataFrame = ttk.Frame(self.containerFrame, borderwidth="3", relief="groove")
        self.dataFrame.pack(fill="both", expand="1")
        self.dataFrame.grid_rowconfigure("0", weight="1")                    #makes cardFrame and selectFrame expand equally with window vertically
        self.dataFrame.grid_columnconfigure("0", weight="2")                 #makes cardFrame (should be column 0) expand horizontally, larger than...
        self.dataFrame.grid_columnconfigure("1", weight="1")                 #selectFrame(should be column 1). The different weights give them correct size
        
        #cardFrame is the left frame that will display the fields and data stored in a randomly selected card
        #IDEA: add button that allows user to re-roll to display a different card as an example.
        self.cardFrame = ttk.Frame(self.dataFrame, borderwidth="3", relief="groove")
        self.cardFrame.grid(column="0", row="0", sticky="NEWS")
        self.cardFrameLabel = ttk.Label(self.cardFrame, anchor="w", justify="left", text="This is a preview of the fields and text available from your cards:")
        self.cardFrameLabel.pack(anchor="w")
        
        #selectFrame is the right frame that will give the user the option to select which fields will be taken from the cards in the deck and used in the conversion
        self.selectFrame = ttk.Frame(self.dataFrame, borderwidth="3", relief="groove")
        self.selectFrame.grid(column="1", row="0", sticky="NEWS")
        self.selectFrameLabel = ttk.Label(self.selectFrame, wraplength="200", text="Select which fields from your deck contain the following information:")
        self.selectFrameLabel.pack()
        
        #chooseFrame contains the combo boxes and their label frames that will display and allow the selection of indicated fields from the selected deck
        self.chooseFrame = ttk.Frame(self.selectFrame, borderwidth="3", relief="groove")
        self.chooseFrame.pack(fill="both", expand="1")
       
        self.combolist = Tkinter.StringVar(self.chooseFrame)
        self.combolist = DeckConverter.test_func()
        
        self.vocabLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Vocab Word:", borderwidth="3", relief="groove")               #vocabulary word
        self.vocabLabelFrame.pack(fill="both", expand="1")
        self.combobox = ttk.Combobox(self.vocabLabelFrame)
        self.combobox.pack(anchor="center", expand="1")
        
        self.TransLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Translation of Vocab:", borderwidth="3", relief="groove")     #translation of vocab word
        self.TransLabelFrame.pack(fill="both", expand="1")
        self.combobox = ttk.Combobox(self.TransLabelFrame)
        self.combobox.pack(anchor="center", expand="1")
        
        self.PronunLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Pronunciation of Vocab:", borderwidth="3", relief="groove")  #pronunciation of vocab word
        self.PronunLabelFrame.pack(fill="both", expand="1")
        self.combobox = ttk.Combobox(self.PronunLabelFrame)
        self.combobox.pack(anchor="center", expand="1")
        
        #runFrame contains the button to run the conversion program on the deck and displays text indicating completion of the run
        self.runFrame = ttk.Frame(self.selectFrame, borderwidth="3", relief="groove")
        self.runFrame.pack(fill="both", expand="1")
        self.runButton = ttk.Button(self.runFrame, text="Convert Deck", command=DeckConverter.convert_deck)
        self.runButton.pack(fill="both", expand="1")
        self.runLabel = ttk.Label(self.runFrame, text="Your deck has been converted.", font="bold", foreground="#24a124", anchor="center")
        #self.runLabel.pack(fill="both", expand="1")    TODO: Write logic to make this label appear only on program completion
        
        