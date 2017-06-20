/*
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
*/
/* flips an elements display from on to off or visa-versa, and toggle's the next element's display back to on */
function flip(item_list, index, cycle){
    item_list[index].style.display = "none";
    if ((index + 1) < item_list.length){
        item_list[index + 1].style.display = "block";
    } else if (cycle){
        item_list[0].style.display = "block";
    }
}

/* Iterates through the list of display elements and book elements, showing only one display and one book at a time */
async function rotate(){
    var displays = document.getElementsByClassName("display")
    var time_delay = 3000;
    while(true){  /* infinite loop for infinite cycling */
        for(var display_counter = 0; display_counter < displays.length; display_counter++){
            var book_counter;
            var books = displays[display_counter].getElementsByClassName("book");
            books[0].style.display = "block";
            time_delay = parseInt(displays[display_counter].dataset.time) * 1000;

            for(book_counter = 0; book_counter < books.length; book_counter++){
                // give people time to view the book
                await new Promise(resolve => setTimeout(resolve, time_delay));
                flip(books, book_counter, false);
            }
            // give people time to view the last book in the previous display
            if (book_counter != books.length){
                await new Promise(resolve => setTimeout(resolve, time_delay));
            }
            flip(displays, display_counter, true);
        }
    }
}

window.onload = rotate();