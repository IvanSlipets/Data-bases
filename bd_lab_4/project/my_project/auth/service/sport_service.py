from project.my_project.auth.dao.sport_dao import SportDAO
from project.my_project.auth.domain.sport import Sport

class SportService:

    def __init__(self):
        self.sport_dao = SportDAO()

    def get_all_sports(self):
        """Отримує список усіх видів спорту."""
        return self.sport_dao.get_all()

    def get_sport_by_id(self, sport_id):
        """Отримує вид спорту за його унікальним ID."""
        return self.sport_dao.get_by_id(sport_id)
    
    def get_sport_with_athletes(self, sport_id):
        """
        Отримує вид спорту за ID, включаючи список усіх пов'язаних з ним спортсменів. Зв’язок M:1 (один вид спорту має багато спортсменів.
        """
        sport = self.sport_dao.get_by_id(sport_id)
        return sport

    def create_sport(self, sport_data):
        """Створює новий вид спорту в базі даних."""
        new_sport = Sport(**sport_data)
        self.sport_dao.create(new_sport)
        return new_sport

    def update_sport(self, sport_id, new_data):
        """Оновлює дані виду спорту за його ID."""
        return self.sport_dao.update(sport_id, new_data)

    def delete_sport(self, sport_id):
        """Видаляє вид спорту за його ID."""
        return self.sport_dao.delete(sport_id)