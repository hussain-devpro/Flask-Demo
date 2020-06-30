from flask import Blueprint

from . import routes

# import eDBS.basic.routes  # noqa: F401

blueprint = Blueprint(
    'basic_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/basic'
)
