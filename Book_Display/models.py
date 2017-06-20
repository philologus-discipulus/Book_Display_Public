'''
    Copyright (C) 2017  David Baron (written in California)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import xml.etree.ElementTree as ET
from os import pathsep

# name of the file with xml markup of the displays
file_name = "book_display_information.xml"

# path to the file with the xml markup of the displays
file_location = ""

# models an individual book and a review of it, if applicable
class Book:

    # takes in the xml of a book, and creates an object from it
    def __init__(self, b):
        self.title = b.findtext("title")
        self.author = b.findtext("author")
        self.image_location = "pictures/" + b.findtext("image_name") if b.findtext("image_name") else ""
        self.review = b.findtext("review")
        self.review_author = b.findtext("review_author")


# models a set of books that together create a display
class Display:
    # title is the book's title
    
    # book_time is the amount of time (in minutes) to spend on each book
    
    # books are the set of books in a display

    # takes in the xml of a display and creates an object from it
    def __init__(self, d):
        self.title = d.findtext("metadata/display_title")
        self.book_time = int(d.findtext("metadata/book_time")) if int(len(d.findtext("metadata/book_time"))) else 1
        self.books = [Book(b) for b in d.findall("book")]



# models a series of displays
class DisplayGroup:
    # library is the library hosting this program

    # library_message is a message from the librarians

    # title is the title of the page used to host the displays

    # displays is the list of displays

    # takes in the xml of a series of displays and the series' metadata and creates an object from it
    def __init__(self):
        tree = ET.parse(pathsep.join([file_location, file_name])) if file_location else ET.parse(file_name)
        root = tree.getroot()

        self.library = root.findtext("metadata_displays/library_name")
        self.library_message = root.findtext("metadata_displays/library_message")
        self.title = root.findtext("metadata_displays/page_title")
        self.displays = [Display(d) for d in root.findall("display")]

# the displays
loaded_displays = DisplayGroup()
