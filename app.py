from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index() -> str:
	return 'Hello, World!'


@app.route('/ping')
def ping() -> str:
	return 'pong'


@app.post('/users')
def create_user() -> Response:
	return Response('User created', status=201)


@app.delete('/users/<user_id>')
def delete_user(user_id: int) -> Response:
	try:
		int(user_id)
		return Response(f'User {user_id} deleted', status=200)
	except ValueError:
		return Response(f'User {user_id} not found', status=404)


if __name__ == '__main__':
	app.run("localhost", 5000, debug=True, threaded=True, use_reloader=False)
