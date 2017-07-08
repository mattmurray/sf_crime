#!flask/bin/python
from app import app
app.run(debug=True)


# this script imports the app variable from the app package and invokes
# its run method to start the server.