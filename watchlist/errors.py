from watchlist import app

from flask import render_template
from watchlist.models import User

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('/errors/404.html'), 404

@app.errorhandler(400)
def page_not_found(e):
    user = User.query.first()
    return render_template('/errors/400.html'), 400

@app.errorhandler(500)
def page_not_found(e):
    user = User.query.first()
    return render_template('/errors/500.html'), 500