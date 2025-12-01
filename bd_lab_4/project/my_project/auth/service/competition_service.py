from project.my_project.auth.dao.competition_dao import CompetitionDAO
from project.my_project.auth.domain.competition import Competition, CompetitionParticipation

class CompetitionService:
    def __init__(self):
        self.competition_dao = CompetitionDAO()

    # COMPETITION CRUD

    def get_all_competitions(self):
        """Отримує список усіх змагань."""
        return self.competition_dao.get_all()

    def get_competition_by_id(self, competition_id):
        """Отримує змагання за його унікальним ID."""
        return self.competition_dao.get_by_id(competition_id)

    def create_competition(self, competition_data):
        """Створює нове змагання в базі даних."""
        new_competition = Competition(**competition_data)
        return self.competition_dao.create(new_competition)

    def update_competition(self, competition_id, update_data):
        """Оновлює дані змагання за його ID."""
        return self.competition_dao.update(competition_id, update_data)

    def delete_competition(self, competition_id):
        """Видаляє змагання за його ID."""
        return self.competition_dao.delete(competition_id)

    # COMPETITION PARTICIPATION CRUD (M:M зв'язок)

    def get_competition_with_participants(self, competition_id):
        """Отримує змагання разом зі списком його учасників."""
        return self.competition_dao.get_competition_with_participants(competition_id)

    def get_participation_by_id(self, participation_id):
        """Отримує запис участі за ID."""
        return self.competition_dao.get_participation_by_id(participation_id)

    def create_participation(self, data):
        """Створює запис в стикувальній таблиці (реєстрація спортсмена на змагання)."""
        return self.competition_dao.create_participation(data)

    def update_participation(self, participation_id, update_data):
        """Оновлює запис участі (наприклад, змінює роль або результат)."""
        return self.competition_dao.update_participation(participation_id, update_data)

    def delete_participation(self, participation_id):
        """Видаляє запис участі."""
        return self.competition_dao.delete_participation(participation_id)