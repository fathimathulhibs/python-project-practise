# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:41:00 2026

@author: nazyh
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

students = []

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Add student
@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify(students)

# Get all students
@app.route("/students")
def get_students():
    return jsonify(students)

# Delete student
@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)