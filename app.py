from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def Hello():
	return 'hello but0n, comming soon!'
@app.route('/log/<int:id>')
def log(id):
	if id == 2704:
		return 's'
	else:
		return 'erro :)'

if __name__ == '__main__':
	app.run()
