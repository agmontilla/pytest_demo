import pytest
import json
from http import HTTPStatus
from flask import url_for


class TestDummy:

    ENDPOINT = "dummy.dummy_dummy"

    def test_with_fixture(self, client, invalid_payloads):

        response = client.post(
            url_for(self.ENDPOINT),
            data=invalid_payloads,
            content_type="application/json",
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST

    # @pytest.mark.parametrize(
    #     "payload", [(json.dumps({"foo": 1})), (json.dumps({"bar": 1}))]
    # )
    # def test_with_parametrize(self, client, payload):

    #     response = client.post(
    #         url_for(self.ENDPOINT),
    #         data=payload,
    #         content_type="application/json",
    #     )

    #     assert response.status_code == HTTPStatus.BAD_REQUEST

    # def test_1(self, client):

    #     response = client.post(
    #         url_for(self.ENDPOINT),
    #         data=json.dumps({"foo": 1}),
    #         content_type="application/json",
    #     )

    #     assert response.status_code == HTTPStatus.BAD_REQUEST

    # def test_2(self, client):

    #     response = client.post(
    #         url_for(self.ENDPOINT),
    #         data=json.dumps({"bar": 1}),
    #         content_type="application/json",
    #     )

    #     assert response.status_code == HTTPStatus.BAD_REQUEST
