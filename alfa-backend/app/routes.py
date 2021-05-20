from flask import request, json, jsonify
from app import app
from sqlalchemy import desc
from sqlalchemy.ext.declarative import DeclarativeMeta
from app.models import Student
from app import db


@app.route('/')
def hello():
    return {
        "data": "hello Wprd"
    }



@app.route("/enter", methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        request_data = json.loads(request.data)
        data = request_data["data"]

        name = data["name"]
        roll_no = data["rollNum"]
        maths = int(data["maths"])
        physics = int(data["phy"])
        chemestry = int(data["chem"])
        total = int(data["total"])
        percentage = int(data["percentage"])
        entry = Student(name=name, roll_no=roll_no, maths_score=maths, chemestry_score=chemestry, physics_score=physics, total=total, percentage=percentage)
        db.session.add(entry)
        db.session.commit()
        print("submitted")
    return "yes"

def student_serializer(data):
    return {
        "name": data.name,
        "roll_no": data.roll_no,
        "maths_score": data.maths_score,
        "physics_score": data.physics_score,
        "chemestry_score": data.chemestry_score,
        "total": data.total,
        "percentage": data.percentage
    }

@app.route('/get_data', methods=["GET"])
def get_data():
    data = Student.query.order_by(Student.percentage.desc())
    return jsonify([*map(student_serializer, data)])
