from app import db
from datetime import date


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    time_posted = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"{self.id} {self.task}"
