'''
Created on Aug 14, 2017

@author: Daphne
'''

import Tkinter
import ttk

class GameGUI(object):
    '''
    This class contains the GUI for the Vocab GrabBag game. It will display a
    stat frame with info regarding the user's deck and previous plays, as well
    as the frames involved in displaying the vocab and drag and drop effects.
    '''


    def __init__(self, master):
        self.game_GUI_root = Tkinter.Toplevel(master)
        self.game_GUI_root.title("Vocab GrabBag")
        self.game_GUI_root.minsize(width="640", height="360")                   #a minimum 16:9 aspect ratio I chose based on personal preference
        
        #The skeleton of the GUI:
        #containerFrame is outermost frame of all frames within master window
        self.containerFrame = ttk.Frame(self.game_GUI_root)
        self.containerFrame.pack(fill="both", expand="1")                       #expands all direction to fill window resize
        
        #menuFrame is thin frame at top of containerFrame containing only Menu button
        #IDEA: maybe include info about where in deck you are, and where in set you are? (though breaks dynamicFrame naming logic)
        self.menuFrame = ttk.Frame(self.containerFrame, borderwidth="3", relief="groove")
        self.menuFrame.pack(fill="x", side="top")                               #intended to always be on top and only expand horizontally
        self.toMenuButton = ttk.Button(self.menuFrame, text="Back to Menu")
        self.toMenuButton.pack(side="left")                                     #button left-justified
        
        #dynamicFrame contains the frame that holds the dynamic info, such as the game itself and the status sidebar
        self.dynamicFrame = ttk.Frame(self.containerFrame, borderwidth="3", relief="groove")
        self.dynamicFrame.pack(fill="both", expand="1")                         #intended to fill all space not occupied by menuFrame
        self.dynamicFrame.grid_rowconfigure("0", weight="1")                    #makes gameFrame and statusFrame expand with window vertically
        self.dynamicFrame.grid_columnconfigure("0", weight="4")                 #makes gameFrame (should be column 0) expand horizontally, larger than...
        self.dynamicFrame.grid_columnconfigure("1", weight="1")                 #statusFrame(should be column 1). The different weights give them correct size
        
        #gameFrame contains the two frames that display the words and facilitate dragging and dropping
        self.gameFrame = ttk.Frame(self.dynamicFrame, borderwidth="3", relief="groove")
        self.gameFrame.grid(column="0", row="0", sticky="NEWS")                 #assigns gamesFrame to first column of dynamicFrame's grid. Expands in all directions
            
        #Where the meat of the stats are:
        #statusFrame is right sidebar that displays stats such as highscore, previous score, and the timer
        self.statusFrame = ttk.Frame(self.dynamicFrame, borderwidth="3", relief="groove")
        self.statusFrame.grid(column="1", row="0", sticky="NEWS")               #assigns statusFrame to second column of dynamicFrame's grid. Expands in all directions
        self.bestsLabel = ttk.Label(self.statusFrame, text="Your Stats")
        self.bestsLabel.pack()
        
        #Where the meat of the game is:
        #dropFrame is the top box that contains the words in that the user must match to. This will be where matches are dropped into
        self.dropFrame = ttk.Frame(self.gameFrame, borderwidth="3", relief="groove")
        self.dropFrame.pack(fill="both", expand="1")
        self.dropLabel = ttk.Label(self.dropFrame, text="Drop Here")
        self.dropLabel.pack()
        
        #dragFrame is the bottom box that contains the words from which the user chooses the matches. Matches will be clicked and dragged away from here
        self.dragFrame = ttk.Frame(self.gameFrame, borderwidth="3", relief="groove")
        self.dragFrame.pack(fill="both", expand="1")
        self.dragLabel = ttk.Label(self.dragFrame, text="Drag This")
        self.dragLabel.pack()

#The following function is a partial WIP that may be unnecessary in the future:
#Turns one set of cards from deck file into a python list:
#first: first card in practice set.    #size: size of practice set
#def listify_deck_set( deck_file, first, size ):
#    deck = open(deck_file)
#    output = open('testfile.txt', 'w')
#    
#    for line in range(first, size+1):   #end condition is non-inclusive, therefore must add 1 to size in loop params
#        line = deck.readline()
#        #data = re.split(r'^[a-zA-Z0-9]*$', line)    #put this in try block
#        #print data
#        #output.write(data)
#        
#    deck.close()
#    output.close()
    