from project.my_project.utils.db_init import db
from project.my_project.auth.domain.sport import Sport
from project.my_project.auth.domain.athlete import Athlete

class SportDAO:

    def get_all(self):
        """Отримати усі види спорту."""
        return Sport.query.all()

    def get_by_id(self, sport_id):
        """Отримати вид спорту за ID."""
        return Sport.query.get(sport_id)
    
    def get_athletes_by_sport_id(self, sport_id):
        """Вивід даних зі сторони зв’язку M:1: отримати спортсменів за ID виду спорту."""
        sport = Sport.query.get(sport_id)
        return sport.athletes if sport else None

    def create(self, sport):
        """Створити новий вид спорту."""
        db.session.add(sport)
        db.session.commit()

    def update(self, sport_id, new_data):
        """Оновити вид спорту."""
        sport = self.get_by_id(sport_id)
        if sport:
            for key, value in new_data.items():
                setattr(sport, key, value)
            db.session.commit()
            return sport
        return None

    def delete(self, sport_id):
        """Видалити вид спорту."""
        sport = self.get_by_id(sport_id)
        if sport:
            db.session.delete(sport)
            db.session.commit()
            return True
        return False