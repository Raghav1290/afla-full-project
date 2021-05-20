from app import db

class Student(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    name = db.Column(db.String(225), nullable=False)
    roll_no = db.Column(db.String(255), nullable=False)
    maths_score        = db.Column(db.Integer, primary_key=True)
    physics_score = db.Column(db.Integer, nullable=False)
    chemestry_score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Integer, nullable=False)


