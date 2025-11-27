from project.my_project.auth.dao.sport_dao import SportDAO
from project.my_project.auth.domain.sport import Sport

class SportService:

    def __init__(self):
        self.sport_dao = SportDAO()

    def get_all_sports(self):
        return self.sport_dao.get_all()

    def get_sport_by_id(self, sport_id):
        return self.sport_dao.get_by_id(sport_id)
    
    def get_sport_with_athletes(self, sport_id):
        """Отримати вид спорту разом зі списком спортсменів (вивід даних зі сторони M:1)."""
        sport = self.sport_dao.get_by_id(sport_id)
        return sport

    def create_sport(self, sport_data):
        new_sport = Sport(**sport_data)
        self.sport_dao.create(new_sport)
        return new_sport

    def update_sport(self, sport_id, new_data):
        return self.sport_dao.update(sport_id, new_data)

    def delete_sport(self, sport_id):
        return self.sport_dao.delete(sport_id)