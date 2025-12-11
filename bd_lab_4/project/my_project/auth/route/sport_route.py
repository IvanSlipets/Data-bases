from flask import Blueprint, jsonify, request
from project.my_project.auth.service.sport_service import SportService
from project.my_project.auth.domain.sport_dto import SportDTO, SportWithAthletesDTO

sport_bp = Blueprint('sport', __name__)
sport_service = SportService()
sport_dto = SportDTO()
sports_dto = SportDTO(many=True)
sport_with_athletes_dto = SportWithAthletesDTO()

# GET: Вивід усіх видів спорту
@sport_bp.route('/', methods=['GET'])
def get_all_sports():
    sports = sport_service.get_all_sports()
    return jsonify(sports_dto.dump(sports)), 200

# GET: Вивід виду спорту за ID
@sport_bp.route('/<int:sport_id>', methods=['GET'])
def get_sport(sport_id):
    sport = sport_service.get_sport_by_id(sport_id)
    if sport:
        return jsonify(sport_dto.dump(sport)), 200
    return jsonify({'message': 'Sport not found'}), 404

# GET: Вивід виду спорту та його спортсменів (Зв'язок M:1)
@sport_bp.route('/<int:sport_id>/athletes', methods=['GET'])
def get_sport_with_athletes(sport_id):
    sport = sport_service.get_sport_with_athletes(sport_id)
    if sport:
        return jsonify(sport_with_athletes_dto.dump(sport)), 200
    return jsonify({'message': 'Sport not found'}), 404

# POST: Створення
@sport_bp.route('/', methods=['POST'])
def create_sport():
    try:
        sport_data = sport_dto.load(request.json)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    new_sport = sport_service.create_sport(sport_data)
    return jsonify(sport_dto.dump(new_sport)), 201

# PUT: Оновлення даних
@sport_bp.route('/<int:sport_id>', methods=['PUT'])
def update_sport(sport_id):
    try:
        update_data = sport_dto.load(request.json, partial=True)
    except Exception as e:
        return jsonify({'message': 'Invalid data', 'errors': str(e)}), 400

    updated_sport = sport_service.update_sport(sport_id, update_data)
    if updated_sport:
        return jsonify(sport_dto.dump(updated_sport)), 200
    return jsonify({'message': 'Sport not found'}), 404

# DELETE: Видалення даних
@sport_bp.route('/<int:sport_id>', methods=['DELETE'])
def delete_sport(sport_id):
    if sport_service.delete_sport(sport_id):
        return jsonify({'message': f'Sport with ID {sport_id} deleted'}), 204
    return jsonify({'message': 'Sport not found'}), 404