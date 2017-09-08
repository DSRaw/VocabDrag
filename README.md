
**A WIP Drag and Drop Game to aid in learning Kanji**

***2017/8/09 Version 0.0.5a***

Another intermediate commit.

*Changes:*

Cleaned up directory mishap after last commit.
Dynamic resizing of the file path displayed after browsing for a file in the DeckConverter window is now functional.
There is still some junk code and significant refactoring to be done before this can be considered a clean commit.

***2017/8/09 Version 0.0.4a***

*Note:* 
I have realized a need for a change in the version formatting. From this commit onward, I will use the third digit in the naming format to indicate intermediate or non-functional WIP commits where new features are partially complete and there is evidence in the code of them being actively worked on.

Workable versions where chunks of features and code are considered to be completed and in a working state will be indicated by the second digit of the version format.

Release versions considered to have full base-functionality and clean code with no WIP bits strewn about will be indicated by the first digit of the format.

I may retroactively apply this to past version commits, but I must review past commit history to determine how their versions should be revised. Until then, be mindful when seeing the past version numbers.

*Changes:*

Screwed up the filesystem with this commit. Will fix in next commit, coming very soon. Currently, the files outside the KanjiDrag folder are considered to be the most up-to-date files.

This is an intermediate commit. Code is currently not to be considered in a functional state. It will run, but not as intended.

Lots of dirty test variables, functions, and funky logic in this one. About to undergo a major function rewrite and feature update. This commit has a semi-workable new function in the DeckConverter module intended to facilitate the display of the file path after a user selects a file in the DeckConverter GUI. This function needs a logic update to calculate how much of the file path to display based on the pixel-width of the entry widget and characters of the font. Will be deleting, adding, and rewriting a lot of code before the next commit.

**A WIP Drag and Drop Game to aid in learning Kanji**

***2017/5/09 Version 0.0.3a***

*Changes:*

Major feature add to DeckConverter and DeckConverterGUI module

Logic for deck conversion is nearly complete

DeckConverterGUI now achieves the majority of it's display functionality

Some restructure of DeckConverter module and refactoring of DeckConverterGUI class

Test code and placeholder code moderately cleaned up

*Details:*

Deck conversion is now nearly complete in theory. Code parses and manipulates the data from the deck files correctly.

DeckConverterGUI will now display a sample card from the deck and allow a user to chose which fields to use in the conversion.

DeckConverterGUI instantiation logic alleviates many, if not all potential issues with leftover data in DeckConverter module.

DeckConverter module has been refactored to reduce some of the need for global variables.

*Note:*

The DeckConverter module still needs much refinement to catch exceptions and invalid input. It also still needs code that will output the converted deck to a new file. It can also still use a moderate amount of refactoring to tighten up variable access and loops. I anticipate the next commit consisting mainly of adding and refining the above requirements. The next major feature update will likely involve the Game logic and some prefunctory MainMenu code to draft the overall vision of what features the user ought to be able to select and how to include them in the game instance.

***2017/17/08 Version 0.0.2a***

*Changes:*

Several modules added

GUI code moved from main function to new class

Major restucture and renaming

Various test code and placeholder codeadded

*Details:*

Several modules added in effort to improve structure and facilitate a more logical bundling code.

There are now distinct GUI classes for each window of the program, and distinct modules of functions respective to each GUI class.

Some classes, functions, and variables have been renamed to conform to a more pythonic naming convention

There is now a MainMenu window with buttons that allow you to click to open a particular window for viewing.

*Note:*

There is a lot of junky test and placeholder code in several of the modules, due to me jumping between working on several features at once. I anticipate a major module restructuring and feature add in the next version, during which this code will be cleaned up and/or removed. A majority of the GUI skeleton for each window is now complete, and there will soon be more of a focus on the code for the underlying functionality of the program.

***2017/10/08 Version 0.0.1a***

*Changes:*

Added some test variables and values for future utilization with GUI callbacks and program logic

Created new module named deck_converter

Changed version-control naming convention in README

*Details:*

There is currently some test data and some junk data in kanji_main. I have commented out some of the larger changes, but left some of the currently unused, but potentially utilizable variables and data.

the deck_converter module is currently primarily a GUI. It's future use will be to provide a window from which a user can select an Anki deck and convert it into a format more elegantly usable by the KanjiDrag game.

*Note to Self:*

Comments could definitely use a major overhaul to comply with pythonic standards and improve readability/ease in hiding comments

***2017/05/08 Version 0.0.0a***

Committed basic skeleton of GUI.
