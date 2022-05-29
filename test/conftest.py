import pytest
import json

from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


missing_fields_in_payload = (json.dumps({"foo": 1}), json.dumps({"bar": 1}))


@pytest.fixture(params=missing_fields_in_payload)
def invalid_payloads(request):
    return request.param
