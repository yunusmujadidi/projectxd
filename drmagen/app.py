from flask import (
    Flask,
    session,
    redirect,
    url_for,
    render_template,
    render_template_string,
    request,
)
from werkzeug.exceptions import *
from forwardchaining import *

app = Flask(__name__)
app.secret_key = "mbuh iki opo rangerti, tapi kayane penting wkwk"
app.static_folder = "static"
app.url_map.strict_slashes = False

daftarGejala = pertanyaan


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("405.html", awal=url_for("index"))


@app.errorhandler(KeyError)
def key_error(e):
    return render_template("405.html", awal=url_for("index"))


@app.errorhandler(IndexError)
def index_error(e):
    return render_template_string("HAYOLOH KOK ERROR KENAPA? 😞")


@app.errorhandler(NameError)
def name_error(e):
    return render_template_string("HAYOLOH KOK ERROR KENAPA? 😞")


@app.errorhandler(TypeError)
def type_error(e):
    return render_template_string("HAYOLOH KOK ERROR KENAPA? 😞")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", awal=url_for("index"))


@app.route("/")
def index():
    diag = []
    session["diag"] = diag
    session.pop("namaPasien", None)
    return render_template("index.html", link=url_for("index"))


def checkGejala():
    diag = session["diag"]
    if request.form.get("iya"):
        diag.append("y")
        session["diag"] = diag
    if request.form.get("tidak"):
        diag.append("n")
        session["diag"] = diag


@app.route("/maucoba", methods=["POST"])
def maucoba():
    if request.method == "POST":
        name = request.form.get("Name")
        session["namaPasien"] = name
        return render_template("welcome.html", name=name, link=url_for("index"))


@app.route("/mau", methods=["POST"])
def mau():
    if request.method == "POST":
        name = session["namaPasien"]
        return render_template("mau.html", name=name, link=url_for("index"))


@app.route("/gamau", methods=["POST"])
def gamau():
    if request.method == "POST":
        name = session["namaPasien"]
        return render_template("gamau.html", name=name, awal=url_for("index"))


@app.route("/diagnose", methods=["POST", "GET"])
def diagnose():
    diag = session["diag"]
    name = session["namaPasien"]
    pertanyaanke = len(diag)
    pertanyaan = daftarGejala[pertanyaanke]
    return render_template(
        "diagnose.html", pertanyaan=pertanyaan, name=name, link=url_for("index")
    )


@app.route("/hasil", methods=["POST"])
def hasil():
    diag = session["diag"]
    nama = session["namaPasien"]
    if request.method == "POST":
        checkGejala()
        if len(diag) != 17:
            return redirect(url_for("diagnose"))
        else:
            hasil_diag = penyakitnya(forwardchaining(diag))
            return render_template(
                "hasil.html",
                terjangkitPenyakit=hasil_diag[0],
                deskripsiPenyakit=hasil_diag[1],
                awal=url_for("index"),
                nama=nama,
            )


if __name__ == "__main__":
    app.run()
