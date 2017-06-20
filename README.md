# Book_Display_Public
A free, open-source program to help people set up digital displays of books.

Please note, this is copyright to David Baron 2017.

This project is meant to help librarians create digital displays of books.

Please note that, for the purposes of this project (including, but not limited to this README.md file) nothing constitutes a warranty of any kind from me insofar as sections 15 + 16 of the GPL 3.0 are concerned.

Hi All, 
This is basically a file that is meant to describe how to make use of this project. I hope you enjoy it! 
-David

P.S. This advice (along with the project itself) is licensed under the GPL 3.0, and the term "program" used in it refers to any and all files in this project, including this README.md file. So, it's your responsibility to make sure that what you're doing doesn't harm or brick your computer. I don't think that what I've outlined will cause any problems, but it's on you to do your own research and/or to check with your IT department. You use this program and follow any instructions entirely at your own risk.

General Use: The project is intended to be used on a computer with one or more remote, non-touchscreen monitors connected (over wifi) as a display that is then made available to patrons. In order to change the books in the display, simply edit the xml file (instructions are included in the file.) If you want to include a book's cover, put the appropriate picture in the static/pictures folder and include the picture's name in the xml file (book_display_information.xml).  If you want to use more than one monitor, open multiple instances of Firefox and follow the standard steps for assigning different instances of Firefox to each monitor.

Also, keep in mind that you can save the xml document as a backup and swap in existing books, reviews, or displays by editing said document.

Setup: First, install the latest version of python on your system, and remember to set the path variable during setup (if you're using Windows). (https://www.python.org/downloads/release/python-361/) Next, type "pip install flask" (without quotes) at the terminal (or command prompt) in order to install the necessary libraries. After that, cd into the folder holding routes.py and type "python routes.py" (without quotes) to run the site. Then the prompt should give you an address on which the website is running. Open a browser and navigate to that address, and the website should load. (I load it in Firefox.) Please note that this is not actually intended for use as a website; rather, it is intended to be a local display that happens to be in a browser - nothing more.
