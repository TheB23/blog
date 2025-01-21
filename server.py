from flask import Flask , render_template
import requests 
app = Flask(__name__)

def blog_api():	
	base_url = "https://api.npoint.io/c790b4d5cab58020d391"
	response = requests.get(base_url)
	data = response.json()
	return data

@app.route("/")
def home():
	blog_data = blog_api()
	return render_template("index.html", posts = blog_data)
@app.route("/blog/<title>")
def blog(title):
	print(title)
	blog_data = blog_api()
	return render_template("blog.html", posts = blog_data)

if __name__ == "__main__":
	app.run(debug=True)
