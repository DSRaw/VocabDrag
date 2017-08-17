# KanjiDrag
A WIP Drag and Drop Game to aid in learning Kanji

2017/17/08 Version 0.0.2a
  Changes:
  Several modules added
    
  GUI code moved from main function to new class
    
  Major restucture and renaming
    
  Various test code and placeholder codeadded
    
  Details:
  Several modules added in effort to improve struture and facilitate a more logical bundling code.
    
  There are now distinct GUI classes for each window of the program, and distinct modules of functions respective to each GUI class.
    
  Some classes, functions, and variables have been renamed to conform to a more pythonic naming convention
    
  There is now a MainMenu window with buttons that allow you to click to open a particular window for viewing.
    
  Note:
    There is a lot of junky test and placeholder code in several of the modules, due to me jumping between working on several features at once. I anticipate a major module restructuring and feature add in the next version, during which this code will be cleaned up and/or removed. A majority of the GUI skeleton for each window is now complete, and there will soon be more of a focus on the code for the underlying functionality of the program.
    
.    
.

2017/10/08 Version 0.0.1a
  Changes:
  Added some test variables and values for future utilization with GUI callbacks and program logic
  
  Created new module named deck_converter
  
  Changed version-control naming convention in README
  
  Details:
  There is currently some test data and some junk data in kanji_main. I have commented out some of the larger changes, but left some of     the currently unused, but potentially utilizable variables and data.
  
  the deck_converter module is currently primarily a GUI. It's future use will be to provide a window from which a user can select an Anki   deck and convert it into a format more elegantly usable by the KanjiDrag game.

  Note to Self:
  Comments could definitely use a major overhaul to comply with pythonic standards and improve readability/ease in hiding comments

.
.

2017/05/08 Version 0.0.0a
  Committed basic skeleton of GUI.
