from flask import Blueprint
from flask import jsonify, redirect

from flaskapp.models import Project, User, db

bp = Blueprint('web', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='static/web')


@bp.route('/')
def index():
    rv = dict()
    rv['projects'] = [x.__repr__() for x in Project.query.all()]
    rv['users'] = [x.__repr__() for x in User.query.all()]

    return jsonify(rv)


@bp.route('users')
def users():
    usersq = User.query.all()
    rv = dict()
    rv['users'] = [x.__repr__() for x in usersq]
    return jsonify(rv)


@bp.route('add-user/<name>/<email>/<tel>')
def add_user(name, email, tel):
    user = User(name, email, tel)
    db.session.add(user)
    db.session.commit()
    return redirect('/')


@bp.route('projects')
def projects():
    projectsq = Project.query.all()
    rv = dict()
    rv['projects'] = [x.__repr__() for x in projectsq]
    return jsonify(rv)


@bp.route('add-project/<name>/<description>')
def add_project(name, description):
    project = Project(name, description)
    db.session.add(project)
    db.session.commit()
    return redirect('/')
