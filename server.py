from flask import Flask , render_template
import requests 
app = Flask(__name__)

@app.route("/")
def hello():
	return f"Yup working!!!"

@app.route("/blog")
def blog():
	base_url = "https://api.npoint.io/c790b4d5cab58020d391"
	response = requests.get(base_url)
	data = response.json()
	return render_template("blog.html", posts = data, num = 10)

if __name__ == "__main__":
	app.run(debug=True)
