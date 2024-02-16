from flask import Blueprint, render_template

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
@views_blueprint.route('/index')
def index():
    return render_template('view/index.html')

@views_blueprint.route('/about')
def about():
    return render_template('view/about.html')

@views_blueprint.route('/privacy')
def privacy():
    return render_template('view/privacy.html')