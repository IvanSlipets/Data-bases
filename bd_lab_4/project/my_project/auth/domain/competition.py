from project.my_project.utils.db_init import db

class Competition(db.Model):
    __tablename__ = 'competitions'
    competition_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.sport_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    participants = db.relationship('CompetitionParticipation', back_populates='competition', lazy=True)

    def __repr__(self):
        return f"<Competition(id={self.competition_id}, name='{self.name}')>"

class CompetitionParticipation(db.Model):
    __tablename__ = 'competition_participation'
    participation_id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.competition_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(200), nullable=False)
    competition = db.relationship('Competition', back_populates='participants')
    athlete = db.relationship('Athlete', back_populates='participations')

    def __repr__(self):
        return f"<CompetitionParticipation(id={self.participation_id}, competition_id={self.competition_id}, athlete_id={self.athlete_id})>"