from project.my_project.utils.db_init import db

class Sport(db.Model):
    __tablename__ = 'sports'
    sport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Зворотний зв'язок M:1 (один вид спорту має багато спортсменів)
    athletes = db.relationship('Athlete', backref='sport', lazy=True)

    def __repr__(self):
        return f"<Sport(id={self.sport_id}, name='{self.name}')>"