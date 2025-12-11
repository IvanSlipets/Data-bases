from project.my_project.utils.db_init import BaseSchema, fields

class AthleteNoteInsertDTO(BaseSchema):
    athlete_id = fields.Int(required=True)
    note_text = fields.Str(required=True)
    note_date = fields.Date(required=True)
    notes_code = fields.Str(required=True)

class ParticipateByNameDTO(BaseSchema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    competition_name = fields.Str(required=True)
    role = fields.Str(required=True)
    result = fields.Str(required=True)