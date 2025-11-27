from flask import Blueprint, jsonify, request
from project.my_project.auth.service.athlete_service import AthleteService
from project.my_project.auth.domain.athlete_dto import AthleteDTO, AthleteWithSportDTO

athlete_bp = Blueprint('athlete', __name__)
athlete_service = AthleteService()
athlete_dto = AthleteDTO()
athletes_dto = AthleteWithSportDTO(many=True)
athlete_with_sport_dto = AthleteWithSportDTO()

# GET: Вивід усіх спортсменів
@athlete_bp.route('/', methods=['GET'])
def get_all_athletes():
    athletes = athlete_service.get_all_athletes()
    return jsonify(athletes_dto.dump(athletes)), 200

# GET: Вивід спортсмена за ID
@athlete_bp.route('/<int:athlete_id>', methods=['GET'])
def get_athlete(athlete_id):
    athlete = athlete_service.get_athlete_by_id(athlete_id)
    if athlete:
        return jsonify(athlete_with_sport_dto.dump(athlete)), 200
    return jsonify({'message': 'Athlete not found'}), 404

# POST: Вставка даних (Створення)
@athlete_bp.route('/', methods=['POST'])
def create_athlete():
    try:
        # Валідація та завантаження вхідних даних
        athlete_data = athlete_dto.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    new_athlete = athlete_service.create_athlete(athlete_data)
    return jsonify(athlete_with_sport_dto.dump(new_athlete)), 201

# PUT: Обновлення даних
@athlete_bp.route('/<int:athlete_id>', methods=['PUT'])
def update_athlete(athlete_id):
    try:
        # partial=True дозволяє оновлювати лише деякі поля
        update_data = athlete_dto.load(request.json, partial=True)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    updated_athlete = athlete_service.update_athlete(athlete_id, update_data)
    if updated_athlete:
        return jsonify(athlete_with_sport_dto.dump(updated_athlete)), 200
    return jsonify({'message': 'Athlete not found'}), 404

# DELETE: Видалення даних
@athlete_bp.route('/<int:athlete_id>', methods=['DELETE'])
def delete_athlete(athlete_id):
    if athlete_service.delete_athlete(athlete_id):
        # Код 204 No Content зазвичай використовується для успішного DELETE
        return '', 204
    return jsonify({'message': 'Athlete not found'}), 404