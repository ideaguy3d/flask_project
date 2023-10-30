
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/game1")
def game1():
    return render_template("game1.html")

@app.route('/hi')
def hello_world():
    return 'Hello from California! 🐻'


@app.route('/edu')
def edu():
    return render_template("education.html")

# Serve files from the "Build" folder
@app.route('/Build/<path:filename>')
def serve_build(filename):
    return send_from_directory('Build', filename)

# Serve files from the "TemplateData" folder
@app.route('/TemplateData/<path:filename>')
def serve_template_data(filename):
    return send_from_directory('TemplateData', filename)

# eof
