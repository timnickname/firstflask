from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import create_post, get_posts, del_posts

app = Flask(__name__)

CORS(app)

@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		pass

	if request.method == 'POST':
		name = request.form.get('name')
		post = request.form.get('post')
		create_post(name,post)

	posts = get_posts()


	return render_template('index.html', posts=posts)


@app.route('/delete/',methods=['GET','POST'])
def delete():

	if request.method == 'POST':
		number = request.form.getlist('id')
		for n in range(len(number)):
			del_posts(number[n])
		#del_posts(number)

	posts = get_posts()
	return redirect("/", code=302)

if __name__ == '__main__':
	app.run(debug=True)