from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

# Each of these route blocks are referred to as 'Views'
@app.route("/")
def home():
	return "Home Page"

# You can access the pieces of the URL like so:
@app.route("/hello/<username>")
def hello(username):
	return "<h2>Hello %s!</h2>" % username.capitalize()

# The data in the URL can be processed as strings or other data types
@app.route("/post/<int:post_id>")
def show_post(post_id):
	if post_id == 1:
		contents = "A post about Python"
	elif post_id == 2:
		contents = "A post about Flask"
	else:
		contents = """<b>Post not found.</b><br>
			Try one of these:<br>
			<a href="/post/1">Python</a><br>
			<a href="/post/2">Flask</a><br>"""
	return "<h1>Post %d</h1><p>%s</p>" % (post_id, contents)

# Trailing slashes indicate directories (even though they obviously aren't).
# This is the same way a traditional site (html files) would handle the trailing slash.
# Forget the trailing slash, Flask will add it for you.
@app.route("/public/")
def public():
	return """
		This is the public dir with a trailing slash.
		If you <a href='/public'>leave tbe trailing slash out of the url</a>, Flask will add it for you.
		"""
# Add the trailing slash where it is not needed, you will 404.
@app.route("/about")
def about():
	return """
		This is the about page with no trailing slash.
		If you <a href='/about/'>add a trailing slash</a>, Flask will 404.
		"""

# url_for(STRING) can be used to build the URL for a function you have defined.
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

# Retrieving POST data
@app.route("/form", methods=['GET', 'POST'])
def form():
	if request.method == 'POST':
		# show the posted content
		return "this was posted:<br>" + request.form['myinput']
	else:
		# show the form
		return """
			<h2>Form</h2>
			<form action='%s' method='post'>
			<input type='text' name='myinput'>
			<input type='submit'>
			</form>
			""" % url_for('form')

# Retrieving GET data
@app.route("/getdata")
def getdata():
	a_get_param = request.args.get("a_get_param")
	if a_get_param is None:
		return "GET param not provided. <a href='%s?a_get_param=a value'>Try this.</a>" % url_for('getdata')
	else:
		return a_get_param

# Send the name string to the template if it is included.
@app.route('/test/')
@app.route('/test/<name>')
def test(name=None):
	return render_template('test.html', name=name)

# Redirecting /index to /
@app.route('/index')
def index():
	return redirect(url_for('home'))

# HTTP Status Errors (404 page not found)
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
