from flask import Blueprint, jsonify, request
from project.my_project.auth.service.competition_service import CompetitionService
from project.my_project.auth.domain.competition_dto import CompetitionDTO, CompetitionWithParticipantsDTO, CompetitionParticipationDTO

competition_bp = Blueprint('competition', __name__)
competition_service = CompetitionService()
competition_dto = CompetitionDTO()
competitions_dto = CompetitionDTO(many=True)
competition_with_participants_dto = CompetitionWithParticipantsDTO()
participation_dto = CompetitionParticipationDTO()

# COMPETITION CRUD

# GET: Вивід усіх змагань
@competition_bp.route('/', methods=['GET'])
def get_all_competitions():
    competitions = competition_service.get_all_competitions()
    return jsonify(competitions_dto.dump(competitions)), 200

# GET: Вивід змагання за ID
@competition_bp.route('/<int:competition_id>', methods=['GET'])
def get_competition(competition_id):
    competition = competition_service.get_competition_by_id(competition_id)
    if competition:
        return jsonify(competition_dto.dump(competition)), 200
    return jsonify({'message': 'Competition not found'}), 404

# POST: Створення змагання
@competition_bp.route('/', methods=['POST'])
def create_competition():
    try:
        competition_data = competition_dto.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    new_competition = competition_service.create_competition(competition_data)
    return jsonify(competition_dto.dump(new_competition)), 201

# PUT: Оновлення змагання
@competition_bp.route('/<int:competition_id>', methods=['PUT'])
def update_competition(competition_id):
    try:
        update_data = competition_dto.load(request.json, partial=True)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    updated_competition = competition_service.update_competition(competition_id, update_data)
    if updated_competition:
        return jsonify(competition_dto.dump(updated_competition)), 200
    return jsonify({'message': 'Competition not found'}), 404

# DELETE: Видалення змагання
@competition_bp.route('/<int:competition_id>', methods=['DELETE'])
def delete_competition(competition_id):
    if competition_service.delete_competition(competition_id):
        return 'Deleted', 204
    return jsonify({'message': 'Competition not found'}), 404

# M:M ЗВ'ЯЗКИ 

# GET: Вивід змагання та його учасників (Зв'язок M:M)
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

# PUT: Оновлення запису участі за ID
@competition_bp.route('/participate/<int:participation_id>', methods=['PUT'])
def update_participation(participation_id):
    try:
        # Можна оновлювати лише result та role, без athlete_id/competition_id
        update_data = participation_dto.load(request.json, partial=True)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    updated_participation = competition_service.update_participation(participation_id, update_data)
    if updated_participation:
        return jsonify(participation_dto.dump(updated_participation)), 200
    return jsonify({'message': 'Participation not found'}), 404

# DELETE: Видалення запису участі за ID
@competition_bp.route('/participate/<int:participation_id>', methods=['DELETE'])
def delete_participation(participation_id):
    if competition_service.delete_participation(participation_id):
        return '', 204
    return jsonify({'message': 'Participation not found'}), 404