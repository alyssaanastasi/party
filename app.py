from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "docs")

@app.route("/")
def invitation():
    return render_template("invitation.html", hide_navbar=True)

@app.route("/inspiration")
def inspiration():
    return render_template("inspiration.html", hide_navbar=False)

@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    name = None
    response = None
    if request.method == "POST":
        name = request.form.get("name")
        response = request.form.get("response")
    return render_template("rsvp.html", name=name, response=response, hide_navbar=False)

if __name__ == "__main__":
    app.run(debug=True)
