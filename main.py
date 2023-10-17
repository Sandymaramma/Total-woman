from Flask_App.__init__ import create_app

import sys
import os

from Simple_Flask_App import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
