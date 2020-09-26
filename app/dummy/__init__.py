from flask import Blueprint

from flask_restx import Api

from app.dummy.views import dummy_ns

dummy_bp = Blueprint("dummy", __name__, url_prefix="/")
dummy_api = Api(dummy_bp)

dummy_api.add_namespace(dummy_ns)
