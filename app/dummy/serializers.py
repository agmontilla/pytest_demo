from flask_restx import Namespace
from flask_restx import fields

dummy_ns = Namespace("dummy")


dummy_payload_expected = dummy_ns.model(
    "dummy model",
    {
        "foo": fields.Integer(description="foo field", required=True),
        "bar": fields.Integer(description="bar field", required=True),
    },
)
