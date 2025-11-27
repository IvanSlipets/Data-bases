from project.my_project.auth.dao.athlete_dao import AthleteDAO
from project.my_project.auth.domain.athlete import Athlete

class AthleteService:

    def __init__(self):
        self.athlete_dao = AthleteDAO()

    def get_all_athletes(self):
        """Отримати список всіх спортсменів."""
        return self.athlete_dao.get_all()

    def get_athlete_by_id(self, athlete_id):
        """Отримати спортсмена за ID."""
        return self.athlete_dao.get_by_id(athlete_id)

    def create_athlete(self, athlete_data):
        """Створити нового спортсмена."""
        new_athlete = Athlete(**athlete_data)
        self.athlete_dao.create(new_athlete)
        return new_athlete

    def update_athlete(self, athlete_id, new_data):
        """Оновити дані спортсмена."""
        return self.athlete_dao.update(athlete_id, new_data)

    def delete_athlete(self, athlete_id):
        """Видалити спортсмена."""
        return self.athlete_dao.delete(athlete_id)