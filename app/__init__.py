from flask import Flask


# create the application object of class Flask and then
# imports the views module.

app = Flask(__name__)
from app import views

# views is imorted at the end to avoid circular references
# -> views module needs to import the app variable defined 
# in this script -> putting at end avoids circular import error.

# the views are handlers that respond to requests from web
# browsers or other clients. In Flask, handlers are written
# as functions, and each function is mapped to one or more
# request URLs.
