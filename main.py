from flask import Flask, redirect, render_template, send_file

from downloader import Downloader
from fotd import Fotd

app = Flask(__name__, template_folder="html")

app.secret_key = b"Prototaxites"

# TODO
#   -if bored:
#       create example factlist
#    translate rest to en
#       throw all on github


@app.route("/")
def index():
    return redirect("/fotd")


@app.route("/fotd")
def fotd():
    fct = Fotd().get_random_fact_list()
    fact_number = Fotd().get_total_number_of_facts()
    return render_template(
        "facts_section.html", facts=fct, fact_number=fact_number, downloader=Downloader.get()
    )


@app.route("/single_fact")
def single_fact():
    fct = Fotd().get_random_fact_list()
    return render_template("fact.html", facts=fct)


#
# pseudo long running task
@app.route("/fotd/download", methods=["POST"])
def start_archive():
    downloader = Downloader.get()
    downloader.run()
    return render_template("long_runner.html", downloader=downloader)


@app.route("/fotd/download", methods=["GET"])
def archive_status():
    downloader = Downloader.get()
    return render_template("long_runner.html", downloader=downloader)


@app.route("/fotd/download/file", methods=["GET"])
def archive_content():
    downloader = Downloader.get()
    return send_file(downloader.download_file(), ".json", as_attachment=True)


@app.route("/fotd/download", methods=["DELETE"])
def reset_archive():
    downloader = Downloader.get()
    downloader.reset()
    return render_template("long_runner.html", downloader=downloader)


if __name__ == "__main__":
    app.run()
