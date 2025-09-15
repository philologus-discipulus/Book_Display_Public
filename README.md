# Book_Display_Public

## Summary
A free, open-source program to help librarians (and people in general) set up digital displays of books.


## Licensing and Copyright Information
Please note, this project is copyright by David Baron and was created in 2017.  The dependencies of Bootstrap and JQuery (distributed with the project) are copyrighted to their respective authors. Flask (distributed separately) is copyrighted to its respective authors.

The advice contained in repository (along with the project itself) is licensed under the GPL 3.0, and the term "program" used in it refers to any and all files in this project, including this README.md file and the advice contained therein.

Note that various dependencies (eg. Bootstrap, JQuery, and Flask) also have their own licenses.  Note that copies of Bootstrap and JQuery are distributed with this project as permitted by those licenses, but the project as a whole is licensed under the GPL 3.0.  Flask is not distributed with this project, and must be downloaded separately from it.  Thus, its license is not included here.

Please also note that, for the purposes of this project (including, but not limited to this README.md file) nothing constitutes a warranty of any kind from me insofar as sections 15 + 16 of the GPL 3.0 are concerned.

---
- Archived version of Bootstrap License:
  - https://web.archive.org/web/20170519023116/https://github.com/twbs/bootstrap/blob/master/LICENSE
  - https://web.archive.org/web/20250724235916/http://github.com/twbs/bootstrap/archive/v3.3.6.zip

<details>
I've quoted bootstrap's MIT License below from the above-linked zip file.  Please, make sure to double-check and verify.

"
The MIT License (MIT)

Copyright (c) 2011-2015 Twitter, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"
</details>

---

- Archived version of JQuery License:
  - https://web.archive.org/web/20170519023014/https://jquery.org/license/
  - https://web.archive.org/web/20250912023353/https://jquery.com/license/
  - also see: https://code.jquery.com/jquery-1.9.1.min.js and https://code.jquery.com/jquery-1.9.1.js
<details>

Please make sure to check the full license at the links - relevant information may not end up included below.

The quote from the first above link states in part:

"
Projects referencing this document are released under the terms of the MIT license.

The MIT License is simple and easy to understand and it places almost no restrictions on what you can do with the Project.

You are free to use the Project in any other project (even commercial projects) as long as the copyright header is left intact.
"

However, I'm not entirely sure if that is correct.  (See: https://web.archive.org/web/20250914213224/https://stackoverflow.com/questions/25709190/including-jquery-in-a-public-project-license )  The source at the link indicates that one may well be obligated to reproduce and distribute the permission notice in the MIT License as well.  Please note that bootstrap's license is also MIT and is included above; obviously the copyright information must change (see copyright notice in the jquery-1.9.1.js for the notice for JQuery), but I do not see why the permission notice would, given the information at the above links.  Thus, I hope in noting such that I have fulfilled the quoted obligation above and any obligation coming from the license, whichever may apply.  In any event, please refer to JQuery's website for further details.  I am not a lawyer and cannot give legal advice.

</details>

---

## General Purpose
The project is intended to be used on a computer with one or more remote, non-touchscreen monitors connected as a display that is then made available for viewing to patrons. In order to change the books in the display, simply edit the xml file (book_display_information.xml - instructions are included in the file).  If you want to include a book's cover, put the appropriate picture in the static/pictures folder and include the picture's name in the xml file.  If you want to use more than one monitor, open multiple instances of Firefox and follow the standard steps for assigning different instances of Firefox to each monitor.  It is recommened that you do not place the monitors in areas where the general public would be expected to have physical access to them.

Also, keep in mind that you can save the xml document as a backup and swap in existing books, reviews, or displays by editing said document and adding the appropriate pictures to the /static/pictures/ folder.

It is possible to run multiple versions of this project on the same computer on different ports.  This allows one computer to be connected to multiple monitors and to then display different displays in different locations.

## Setup Steps:

### Code Setup 
(1) Install the latest version of python on your system, and remember to set the path variable during setup (if you're using Windows).
(2) Install pip, the python package management system.
(3) Type "pip install Flask" (without quotes) at the terminal (or command prompt) in order to install the necessary libraries. 
(4) Open a terminal (command prompt) window and navigate to the folder holding routes.py
(5) Type "python3 routes.py" or "python routes.py" (without quotes - the python3/python should be the command necessary to run python from the command prompt) to run the site. If you want to specify a port, add the "-p &lt;portnumber&gt;" or "--port &lt;portnumber&gt;" (eg. "python3 routes.py --port 4000") to specify a port.  If you pick a port already in use, this program should fail; you should be able to try again with a different port.
- (5.a) The prompt should then give you an address (some variant of a localhost port - eg. http://127.0.0.1:#### where #### is a four digit number denoting the port) on which the website is running. Open a browser and navigate to that address, and the website should load. (Tested in Firefox.) Please note that this is not actually intended for use as a website; rather, it is intended to be a local display that happens to be in a browser - nothing more.

### Display Customization

Both the content and the aesthetic of the display can be customized.  Please read the entirety of this section before making any changes.

It is recommended that, whenever changing a file, you make an appropriate backup first.

#### Aesthetic

To customize the aesthetic of the display, consider editing the following files:

/static/book_display.css
/templates/book_display_template.html
/templates/frame.html

Note that any content within curly brackets (ie. {}) should not be changed; this is embedded content from the server and is distinct from the surrounding css/html.

It is recommended that you not change any ids, nor any class defined in the html (eg. class = "book"), but rather change the styling of the class in the book_display.css.  The reason for this is that the javascript functions in /static/rotate.js rely on the class name to find certain elements.  The javascript also toggles the display of those elements from "block" to "none" and visa versa to control visibility.

In general, it is safer to change the .css file (book_display.css) than it is to change any .html files, as changing the html has a greater risk of rendering the display inoperable.

#### Display Content

To modify the display content, feel free to change the text in the following xml file: book_display_information.xml
Any new pictures should be added to the /static/pictures/ folder.

When doing so, please note the following:

(1) New &lt;display&gt; elements can be added, provided that all of their child elements, grandchild elements, etc. are preserved with at least one of each type.

(2) Multiple &lt;book&gt; elements can be added, provided that all of their child elements, etc. are preserved with at least one of each type.
- (2.a) At least one &lt;book&gt; element must be present for a &lt;display&gt;, though.
- (2.b) The &lt;image_name&gt; element has a file name in it.  This directly corresponds to the filename of the appropriate picture in the /static/pictures/ folder.  (Eg. &lt;image_name&gt;First_Stock.png&lt;/image_name&gt; corresponds to /static/pictures/First_Stock.png) This tag determines the picture to be shown with a given book.

(3) book_display_information.xml has comments in it helping to explain other xml elements and their purposes.  It is recommended that you read those prior to modifying the file.

(4) As always, it is also recommended that you make backups as necessary.


