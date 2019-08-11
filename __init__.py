from flask import Flask

app = Flask("My App")

@app.route("/")
def hello():
    return "Hello World! from Flask"

if __name__ == "__main__":
	app.run()
