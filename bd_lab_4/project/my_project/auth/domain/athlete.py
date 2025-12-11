from project.my_project.utils.db_init import db
from datetime import date
from project.my_project.auth.domain.competition import CompetitionParticipation

class Athlete(db.Model):
    __tablename__ = 'athletes'
    athlete_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False, default=date.today)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    height_cm = db.Column(db.SmallInteger, nullable=False)
    weight_kg = db.Column(db.Numeric(5, 2), nullable=False)
    participations = db.relationship('CompetitionParticipation', back_populates='athlete', lazy=True)
    # Зв'язок M:1 (багато спортсменів до одного виду спорту)
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.sport_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"<Athlete(id={self.athlete_id}, name='{self.first_name} {self.last_name}')>"
