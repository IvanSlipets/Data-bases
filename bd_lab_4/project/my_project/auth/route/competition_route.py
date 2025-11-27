from flask import Blueprint, jsonify, request
from project.my_project.auth.service.competition_service import CompetitionService
from project.my_project.auth.domain.competition_dto import CompetitionDTO, CompetitionWithParticipantsDTO, CompetitionParticipationDTO

competition_bp = Blueprint('competition', __name__)
competition_service = CompetitionService()
competition_dto = CompetitionDTO()
competition_with_participants_dto = CompetitionWithParticipantsDTO()
participation_dto = CompetitionParticipationDTO()

# GET: Вивід змагання та його учасників (Зв'язок M:M)
# Вивід даних зі стикувальної таблиці
@competition_bp.route('/<int:competition_id>/participants', methods=['GET'])
def get_competition_with_participants(competition_id):
    competition = competition_service.get_competition_with_participants(competition_id)
    if competition:
        return jsonify(competition_with_participants_dto.dump(competition)), 200
    return jsonify({'message': 'Competition not found'}), 404

# POST: Створення запису в стикувальній таблиці
@competition_bp.route('/participate', methods=['POST'])
def create_participation():
    try:
        participation_data = participation_dto.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    new_participation = competition_service.create_participation(participation_data)
    return jsonify(participation_dto.dump(new_participation)), 201

