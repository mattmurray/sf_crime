from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # user = {'nickname': 'Matt'}  # fake user
    return render_template('index.html')

# 2 route dectorators create mappings from URLs '/' and '/index'
