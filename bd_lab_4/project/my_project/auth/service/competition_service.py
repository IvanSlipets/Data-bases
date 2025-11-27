from project.my_project.auth.dao.competition_dao import CompetitionDAO

class CompetitionService:

    def __init__(self):
        self.competition_dao = CompetitionDAO()
    
    def get_competition_with_participants(self, competition_id):
        return self.competition_dao.get_competition_with_participants(competition_id)

    def create_participation(self, data):
        return self.competition_dao.create_participation(data)
