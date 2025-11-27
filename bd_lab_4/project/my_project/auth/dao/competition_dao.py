from project.my_project.utils.db_init import db
from project.my_project.auth.domain.competition import Competition, CompetitionParticipation
from project.my_project.auth.domain.athlete import Athlete
from sqlalchemy.orm import joinedload

class CompetitionDAO:

    def get_all_competitions(self):
        """Отримати усі змагання."""
        return Competition.query.all()
    
    def get_competition_with_participants(self, competition_id):
        """
        Вивід даних зі стикувальної таблиці зв’язку М:М: 
        вивести для кожного суб’єкта з одної таблиці усі суб’єкти другої таблиці, 
        які приєднані до нього (Змагання та його учасники-спортсмени).
        """
        # Використовуємо joinedload для завантаження зв'язаних об'єктів
        return Competition.query.options(
            joinedload(Competition.participants).joinedload(CompetitionParticipation.athlete)
        ).filter_by(competition_id=competition_id).first()

    def get_participation_by_id(self, participation_id):
        """Отримати запис участі за ID."""
        return CompetitionParticipation.query.get(participation_id)

    def create_participation(self, data):
        """Створити запис в стикувальній таблиці."""
        new_participation = CompetitionParticipation(**data)
        db.session.add(new_participation)
        db.session.commit()
        return new_participation
    
