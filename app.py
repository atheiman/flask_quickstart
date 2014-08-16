from flask import Flask
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

if __name__ == "__main__":
	app.run(debug=True)
