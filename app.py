from os import environ

from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)
app.secret_key = b'U\xdd?\x9b91F\x12\xa3\xc84\xa5\nr\xe3\xc5'


@app.route('/')
def hello_world():
	return 'This is another text.'
# print(environ)
@app.route('/hello/')
@app.route('/hello/<string:name>/')
def hello(name=None):
	return render_template('hello_name.html',name=name)
	# return "Hello {}".format(name)

from flask import request

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return "This is post method."
	else:
		return "This is get method"

from werkzeug.utils import secure_filename

@app.route('/upload/',methods=['POST','OPTIONS'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('/home/amit/PycharmProjects/full_stack_python/flask/flask_docs_practices/'+secure_filename(f.filename))
		return "File saved successfully."



if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)
