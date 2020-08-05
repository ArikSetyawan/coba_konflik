from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "hello World"

@app.route('/user')
def user():
	return "ini halaman user"

@app.route("/profile")
def profile():
	return "hello Profile"

if __name__ == "__main__":
	app.run()
