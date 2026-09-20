from flask import Flask, send_from_directory, abort
from pathlib import Path
import threading
import webbrowser
import os

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000

app = Flask(__name__, static_folder=None)

@app.after_request
def add_headers(response):
    # Wichtig für eingebettete YouTube-Player / Fehler 153.
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    # Beim Testen immer die aktuelle Datei laden.
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/")
def home():
    return send_from_directory(ROOT, "index.html")

@app.route("/<path:filename>")
def project_file(filename):
    target = (ROOT / filename).resolve()

    # Nur Dateien innerhalb dieses Projektordners ausliefern.
    try:
        target.relative_to(ROOT)
    except ValueError:
        abort(404)

    if not target.is_file():
        abort(404)

    return send_from_directory(ROOT, filename)

def open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}/")

if __name__ == "__main__":
    print("=" * 62)
    print("Lokaler Flask-Testserver")
    print(f"Adresse: http://{HOST}:{PORT}/")
    print("Beenden: STRG + C")
    print("=" * 62)

    threading.Timer(1.0, open_browser).start()
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)
