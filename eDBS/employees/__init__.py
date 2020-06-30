from flask import Blueprint

from . import routes

# import eDBS.employees.routes  # noqa: F401

blueprint = Blueprint(
    'employees_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/employees'
)
