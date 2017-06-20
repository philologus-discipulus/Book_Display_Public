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

# Archival Notes for Licenses for Flask, Bootstrap, and JQuery

# Flask License: http://flask.pocoo.org/docs/0.12/license/#flask-license (3-Clause BSD)
# archived version of license:
# https://web.archive.org/web/20170519021831/http://flask.pocoo.org/docs/0.12/license/

# Bootstrap License: https://github.com/twbs/bootstrap/blob/master/LICENSE
# archived version of license:
# https://web.archive.org/web/20170519023116/https://github.com/twbs/bootstrap/blob/master/LICENSE

# JQuery License: https://jquery.org/license/
# archived version of license:
# https://web.archive.org/web/20170519023014/https://jquery.org/license/

from flask import Flask, render_template
from models import loaded_displays

app = Flask(__name__)

@app.route("/")

def home_page():
    return render_template("book_display_template.html", display_group = loaded_displays )

if __name__ == "__main__":
    app.run()