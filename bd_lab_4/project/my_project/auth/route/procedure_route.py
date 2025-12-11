from flask import Blueprint, request, jsonify
from project.my_project.auth.service.procedure_service import ProcedureService

procedure_bp = Blueprint('procedure', __name__)
procedure_service = ProcedureService()

# POST: Виклик процедури insert_nonames
@procedure_bp.route('/insert_nonames', methods=['POST'])
def insert_nonames():
    data = request.json
    msg = procedure_service.insert_nonames(data['table'], data['prefix'], data['start'])
    return jsonify({'message': msg})

# POST: Виклик процедури link_athlete_supplement
@procedure_bp.route('/link_athlete_supplement', methods=['POST'])
def link_athlete_supplement():
    data = request.json
    msg = procedure_service.link_athlete_supplement(data['first_name'], data['last_name'], data['supplement_name'])
    return jsonify({'message': msg})

# POST: Виклик параметризованої вставки
@procedure_bp.route('/param_insert', methods=['POST'])
def param_insert():
    data = request.json
    msg = procedure_service.param_insert(data['table'], data['columns'], data['values'])
    return jsonify({'message': msg})


# GET: Виклик агрегатних функцій 'MAX', 'MIN', 'SUM', 'AVG'
@procedure_bp.route('/sp_call_aggregate', methods=['GET'])
def agg_dynamic_route():
    table = request.args.get('table')
    column = request.args.get('column')
    agg = request.args.get('agg')  # 'MAX', 'MIN', 'SUM', 'AVG'
    # Змінено: використовуємо нову назву методу
    value = procedure_service.sp_call_aggregate(table, column, agg) 
    return jsonify({'value': value})


# POST: Виклик процедури split_meals_to_two
@procedure_bp.route('/split_meals_to_two', methods=['POST'])
def split_meals_to_two():
    msg = procedure_service.split_meals_to_two()
    return jsonify({'message': msg})
