from app import app, ping
from enum import Enum


class status_codes(Enum):
	OK = 200
	CREATED = 201
	NOT_FOUND = 404


def test_ping():
	assert ping() == "pong"
	assert type(ping()) == str


def test_ping_endpoint() -> None:
	client = app.test_client()
	res = client.get('/ping')
	assert res.status_code == status_codes.OK.value
	assert res.data == b'pong'


def test_index_endpoint() -> None:
	client = app.test_client()
	res = client.get('/')
	assert res.status_code == status_codes.OK.value
	assert res.data == b'Hello, World!'
	assert res.content_type == 'text/html; charset=utf-8'
	assert type(res.data) == bytes


def test_create_user_endpoint() -> None:
	client = app.test_client()
	res = client.post('/users')
	assert res.status_code == status_codes.CREATED.value
	assert res.data == b'User created'
	assert type(res.data) == bytes


def test_delete_user_endpoint() -> None:
	client = app.test_client()
	res = client.delete('/users/1')
	assert res.status_code == status_codes.OK.value
	assert res.data == b'User 1 deleted'


def test_delete_user_endpoint_with_invalid_id() -> None:
	client = app.test_client()
	res = client.delete('/users/one')
	assert res.status_code == status_codes.NOT_FOUND.value
	assert res.data == b'User one not found'
