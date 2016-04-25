from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def Hello():
	render_template('index.html')
@app.route('/log/<int:id>')
def log(id):
	if id == 2704:
		return 's'
	else:
		return 'erro :)'

if __name__ == '__main__':
	app.run()
