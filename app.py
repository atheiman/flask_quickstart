from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
	return "Home Page"

@app.route("/hello/<username>")
def hello(username):
	return "<h2>Hello %s!</h2>" % username.capitalize()

@app.route("/post/<int:post_id>")
def show_post(post_id):
	if post_id == 001:
		contents = "A post about Python"
	elif post_id == 002:
		contents = "A post about Flask"
	else:
		contents = """<b>Post not found.</b><br>
			Try one of these:<br>
			<a href="/post/001">Python</a><br>
			<a href="/post/002">Flask</a><br>"""
	return "<h1>Post %d</h1><p>%s</p>" % (post_id, contents)

@app.route("/public/")
def public():
	return """
		This is the public dir with a trailing slash.
		If you <a href='/public'>leave tbe trailing slash out of the url</a>, Flask will add it for you.
		"""

@app.route("/about")
def about():
	return """
		This is the about page with no trailing slash.
		If you <a href='/about/'>add a trailing slash</a>, Flask will 404.
		"""

@app.route("/links")
def links():
	return """
		<h2>This is URL building with Flask's <code>url_for()</code> function.</h2>
		<p>Be sure to include: <code>from flask import url_for</code>.</p>
		<p><code>url_for()</code> will return the URL for the function name you pass it as a string. Earlier we defined <code>about()</code> to run for the "/about" route, so <code>url_for('about')</code> will return <code>/about</code>.</p>
		<p><a href='%s'>Public</a></p>
		<p><a href='%s'>About</a></p>
		<p><a href='%s'>Links</a></p>
		<p>All the links above are generated with the <code>url_for()</code> function.</p>
		""" % (url_for('public'), url_for('about'), url_for('links'))

@app.route("/form", methods=['GET', 'POST'])
def form():
	if request.method == 'POST':
		# show the posted content
		return "this was posted"
	else:
		# show the form
		return """
			<h2>Form</h2>
			<form action='%s' method='post'>
			<input type='text' name='myinput'>
			<input type='submit'>
			</form>
			""" % url_for('form')

@app.route('/test/')
@app.route('/test/<name>')
def test(name=None):
    return render_template('test.html', name=name)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
