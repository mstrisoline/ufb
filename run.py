#!/usr/bin/env python

#Run the modularized application
from ufb import app, db

if __name__ == "__main__":
    app.debug =  True
    db.create_all(app=app)
    app.run(debug=True)
