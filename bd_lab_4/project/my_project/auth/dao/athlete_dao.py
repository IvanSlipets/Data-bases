from project.my_project.utils.db_init import db
from project.my_project.auth.domain.athlete import Athlete
from sqlalchemy.orm import joinedload

class AthleteDAO:

    def get_all(self):
        """Отримати усіх спортсменів, завантажуючи пов'язаний вид спорту."""
        return Athlete.query.options(joinedload(Athlete.sport)).all()

    def get_by_id(self, athlete_id):
        """Отримати спортсмена за ID, включаючи вид спорту."""
        return Athlete.query.options(joinedload(Athlete.sport)).get(athlete_id)

    def create(self, athlete):
        """Створити нового спортсмена."""
        db.session.add(athlete)
        db.session.commit()

    def update(self, athlete_id, new_data):
        """Оновити дані спортсмена."""
        athlete = self.get_by_id(athlete_id)
        if athlete:
            for key, value in new_data.items():
                setattr(athlete, key, value)
            db.session.commit()
            return athlete
        return None

    def delete(self, athlete_id):
        """Видалити спортсмена."""
        athlete = self.get_by_id(athlete_id)
        if athlete:
            db.session.delete(athlete)
            db.session.commit()
            return True
        return False