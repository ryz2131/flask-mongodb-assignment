import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-development-key")


def get_mongo_collection():
    """Create a MongoDB client and return the configured collection."""
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI is not configured. Add it to your .env file.")

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # Force a connection check now so connection errors appear during form submission.
    client.admin.command("ping")

    db_name = os.getenv("MONGO_DB_NAME", "flask_assignment")
    collection_name = os.getenv("MONGO_COLLECTION", "submissions")
    return client[db_name][collection_name]


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api")
def api():
    """Read the backend JSON file and return its contents as JSON."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as json_file:
            records = json.load(json_file)
        if not isinstance(records, list):
            raise ValueError("data.json must contain a JSON list.")
        return records, 200
    except (OSError, json.JSONDecodeError, ValueError) as error:
        app.logger.exception("Unable to read API data")
        return {"error": str(error)}, 500


@app.post("/submit")
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="Please complete all fields.",
            form_data={"name": name, "email": email, "message": message},
        ), 400

    document = {"name": name, "email": email, "message": message}

    try:
        collection = get_mongo_collection()
        collection.insert_one(document)
        return redirect(url_for("success"))
    except (PyMongoError, RuntimeError) as error:
        app.logger.exception("MongoDB submission failed")
        return render_template(
            "index.html",
            error=f"Could not save your data: {error}",
            form_data=document,
        ), 500


@app.get("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=True)
