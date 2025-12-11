from project.my_project.utils.db_init import db
from project.my_project.auth.domain.competition import Competition, CompetitionParticipation
from sqlalchemy.orm import joinedload

class CompetitionDAO:

    def get_all(self):
        """Отримати усі змагання."""
        return Competition.query.all()
    
    def get_by_id(self, competition_id):
        """Отримати змагання за ID."""
        return Competition.query.get(competition_id)
    
    def create(self, competition):
        """Створити нове змагання."""
        db.session.add(competition)
        db.session.commit()
        return competition

    def update(self, competition_id, new_data):
        """Оновити змагання."""
        competition = self.get_by_id(competition_id)
        if competition:
            for key, value in new_data.items():
                setattr(competition, key, value)
            db.session.commit()
            return competition
        return None

    def delete(self, competition_id):
        """Видалити змагання."""
        competition = self.get_by_id(competition_id)
        if competition:
            db.session.delete(competition)
            db.session.commit()
            return True
        return False
    
    # Вивід даних зі стикувальної таблиці зв’язку М:М: 
    def get_competition_with_participants(self, competition_id):
        """
        Вивести для кожного суб’єкта з одної таблиці усі суб’єкти другої таблиці, 
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
    
    def update_participation(self, participation_id, new_data):
        """Оновити запис участі."""
        participation = self.get_participation_by_id(participation_id)
        if participation:
            for key, value in new_data.items():
                # Уникаємо оновлення primary key та foreign keys через PUT
                if key not in ['participation_id', 'athlete_id', 'competition_id']:
                    setattr(participation, key, value)
            db.session.commit()
            return participation
        return None

    def delete_participation(self, participation_id):
        """Видалити запис участі."""
        participation = self.get_participation_by_id(participation_id)
        if participation:
            db.session.delete(participation)
            db.session.commit()
            return True
        return False