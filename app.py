from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world, this is flask app home page"

if __name__ == "__main__":
  app.run(debug=True)
