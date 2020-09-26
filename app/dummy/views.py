from flask_restx import Resource
from app.dummy.serializers import dummy_ns, dummy_payload_expected


@dummy_ns.route("/")
class Dummy(Resource):
    @dummy_ns.expect(dummy_payload_expected, validate=True)
    def post(self):
        foo, bar = dummy_ns.payload["foo"], dummy_ns.payload["bar"]
        return {"message": "the sum is {}".format(foo + bar)}
