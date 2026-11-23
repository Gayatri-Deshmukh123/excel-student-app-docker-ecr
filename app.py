
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.getenv("EXCEL_FILE", os.path.join(BASE_DIR, "students.xlsx"))


def load_students():
    try:
        df = pd.read_excel(EXCEL_FILE)
        df.columns = df.columns.str.strip()
        df = df.fillna("")

        print("Loaded columns:", df.columns.tolist())
        print("Loaded student data:", df.to_dict(orient="records"))

        return df.to_dict(orient="records")

    except Exception as e:
        print("Error reading Excel:", e)
        return []


@app.route("/")
def home():
    students = load_students()

    search = request.args.get("search", "").strip().lower()

    if search:
        students = [
            student for student in students
            if search in str(student.get("Name", "")).lower()
            or search in str(student.get("Course", "")).lower()
            or search in str(student.get("Student ID", "")).lower()
        ]

    total_students = len(load_students())

    return render_template(
        "index.html",
        students=students,
        total_students=total_students,
        search=search
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



