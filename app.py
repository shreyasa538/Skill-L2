"""
Simple Flask application for DevOps Lab demo.
"""

from flask import Flask
import webbrowser
import threading

app = Flask(__name__)


@app.route("/")
def home():
    """Return a welcome message for the DevOps Lab."""
    return "Welcome to DevOps Lab - Version 5"


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    # Start browser in a separate thread
    threading.Timer(1.0, open_browser).start()
    app.run()
