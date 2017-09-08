'''
Created on Aug 6, 2017

@author: Daphne
'''
import Tkinter
import tkFont
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
    
    top = object    #the topLevel window that is MainMenuGUI
           
    #Below is the GUI framework for DeckConverter's window      
    def __init__(self, master):                                                 #root should be root window of the main window of the GUI
        DeckConverter.set_instance(self)        
                   
        self.deckConverterRoot = Tkinter.Toplevel(master)                       #Makes DeckConverter window a separate window linked to the main GUI
        self.deckConverterRoot.title("Convert a Deck")
        self.deckConverterRoot.resizable("true","true")                         #might set this to false later to make this a fixed-width window.
        self.deckConverterRoot.minsize(width="640", height="360")               #a minimum 16:9 aspect ratio I chose based on personal preference
        
        #The following function destroys current deck converter object and starts a fresh object. Called when user chooses to convert another deck.
        def new_DeckConverterGUI(top = master):                                 #passes the same MainMenuGUI instance as master to new DeckConverterGUI instance
            self.deckConverterRoot.destroy()
            DeckConverterGUI(top)
        
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
        
        self.file_path = Tkinter.StringVar()
        self.file_path.set("No file selected.")
        self.entry_font = tkFont.Font(family="TkFixedFont", size="10")
        
        self.pathEntry = ttk.Entry(self.browseFrame, textvariable=self.file_path, font=self.entry_font, state="readonly")            #Will display the file path of selected file
        self.pathEntry.pack(side="left", fill="x", expand="1")
        self.pathEntry.bind("<Configure>", lambda event : DeckConverter.resize_path_display(self.pathEntry))    #TODO Use the format to replace curObj convention
        
        #dataFrame will contain the two frames that display an example card of the deck and allow a user to select data from it
        self.dataFrame = ttk.Frame(self.containerFrame, borderwidth="3", relief="groove")
        self.dataFrame.pack(fill="both", expand="1")
        self.dataFrame.grid_rowconfigure("0", weight="1")                       #makes cardFrame and selectFrame expand equally with window vertically
        self.dataFrame.grid_columnconfigure("0", weight="2")                    #makes cardFrame (should be column 0) expand horizontally, larger than...
        self.dataFrame.grid_columnconfigure("1", weight="1")                    #selectFrame(should be column 1). The different weights give them correct size
        
        #cardFrame is the left frame that will display the fields and data stored in a randomly selected card
        #IDEA: add button that allows user to re-roll to display a different card as an example.
        self.cardFrame = ttk.Frame(self.dataFrame, borderwidth="3", relief="groove")
        self.cardFrame.grid(column="0", row="0", sticky="NEWS")
        self.cardFrameLabel = ttk.Label(self.cardFrame, anchor="w", justify="left", text="This is a preview of the fields and text available from your cards:")
        self.cardFrameLabel.pack(anchor="w")
        self.rerollButton = ttk.Button(self.cardFrame, text="Display a different example", command=DeckConverter.re_roll)
        self.rerollButton.pack(side="bottom", fill="both")
        
        #exampleFrame is the frame that will display the fields and corresponding data available by the deck chosen by the user
        self.exampleFrame = ttk.Frame(self.cardFrame, borderwidth="3", relief="groove")
        
        xscrollbar = ttk.Scrollbar(self.exampleFrame, orient="horizontal")
        yscrollbar = ttk.Scrollbar(self.exampleFrame, orient="vertical")
        
        self.exampleCanvas = Tkinter.Canvas(self.exampleFrame)
        self.exampleCanvas.config(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
        self.textID = self.exampleCanvas.create_text(10,10,anchor="nw", font=12)
        
        self.exampleFrame.pack(fill="both", expand="1")
        xscrollbar.pack(side="bottom", fill="x")
        yscrollbar.pack(side="right", fill="y")
        self.exampleCanvas.pack()
        xscrollbar.config(command=self.exampleCanvas.xview)
        yscrollbar.config(command=self.exampleCanvas.yview)
        
        #selectFrame is the right frame that will give the user the option to select which fields will be taken from the cards in the deck and used in the conversion
        self.selectFrame = ttk.Frame(self.dataFrame, borderwidth="3", relief="groove")
        self.selectFrame.grid(column="1", row="0", sticky="NEWS")
        self.selectFrameLabel = ttk.Label(self.selectFrame, wraplength="200", text="Select which fields from your deck contain the following information:")
        self.selectFrameLabel.pack()
        
        #chooseFrame contains the combo boxes and their label frames that will display and allow the selection of indicated fields from the selected deck
        self.chooseFrame = ttk.Frame(self.selectFrame, borderwidth="3", relief="groove")
        self.chooseFrame.pack(fill="both", expand="1")
       
        self.vocabLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Vocab Word:", borderwidth="3", relief="groove")               #vocabulary word
        self.vocabLabelFrame.pack(fill="both", expand="1")
        self.combo_choice = Tkinter.StringVar(self.vocabLabelFrame)                                                                 #variable that will store the selected choice
        self.vocabCombobox = ttk.Combobox(self.vocabLabelFrame)
        self.vocabCombobox.pack(anchor="center", expand="1")
        
        self.transLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Translation of Vocab:", borderwidth="3", relief="groove")     #translation of vocab word
        self.transLabelFrame.pack(fill="both", expand="1")
        self.combo_choice = Tkinter.StringVar(self.transLabelFrame)
        self.transCombobox = ttk.Combobox(self.transLabelFrame)
        self.transCombobox.pack(anchor="center", expand="1")
        
        self.pronunLabelFrame = ttk.LabelFrame(self.chooseFrame, text="Pronunciation of Vocab:", borderwidth="3", relief="groove")  #pronunciation of vocab word
        self.pronunLabelFrame.pack(fill="both", expand="1")
        self.combo_choice = Tkinter.StringVar(self.pronunLabelFrame)
        self.pronunCombobox = ttk.Combobox(self.pronunLabelFrame)
        self.pronunCombobox.pack(anchor="center", expand="1")
        
        #runFrame contains the button to run the conversion program on the deck and displays text indicating completion of the run
        self.runFrame = ttk.Frame(self.selectFrame, borderwidth="3", relief="groove")
        self.runFrame.pack(fill="both", expand="1")
        self.runButton = ttk.Button(self.runFrame, text="Convert Deck", command=DeckConverter.convert_deck)
        self.runButton.pack(fill="both", expand="1")
        
        #The following button and label will only appear after the program has been run once. They will give the user the choice to convert a different deck
        self.runLabel = ttk.Label(self.runFrame, text="Your deck has been converted.", font="bold", foreground="#24a124", anchor="center")
        self.rerunButton = ttk.Button(self.runFrame, text="Convert Another Deck?", command=new_DeckConverterGUI)
        
        