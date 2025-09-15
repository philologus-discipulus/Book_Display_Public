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

# Archived version of Flask License 
# (note: website appears to have changed since 2017; since Flask is hosted externally and needs 
#  to be installed, please check the license associated with the relevant package to 
#  be sure that terms and conditions have not changed - I include the link below merely
#  to illustrate the version of Flask against which this project was originally developed):
# https://web.archive.org/web/20170519021831/http://flask.pocoo.org/docs/0.12/license/

# Archived version of Bootstrap License:
# https://web.archive.org/web/20170519023116/https://github.com/twbs/bootstrap/blob/master/LICENSE

# Archived version of JQuery License:
# https://web.archive.org/web/20170519023014/https://jquery.org/license/

from flask import Flask, render_template
from models import loaded_displays

import argparse

localhost = '127.0.0.1'

argsParser = argparse.ArgumentParser()
argsParser.add_argument("-p", '--port', type=int, help=f"Specify the port for localhost ({localhost}) on which the Book Display Project is to run.  Eg. specifying '5000' results in the Book Display Project running on 'http://{localhost}:5000'.  Note that this is not meant to be used as a website, merely using the browser as a local means of displaying the project.")

arguments = argsParser.parse_args()

app = Flask(__name__)

@app.route("/")

def home_page():
    return render_template("book_display_template.html", display_group = loaded_displays )

if __name__ == "__main__":
    app.run(host=localhost, port=arguments.port if arguments.port else 5000, debug=False)
