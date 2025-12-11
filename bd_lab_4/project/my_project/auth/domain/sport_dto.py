from project.my_project.utils.db_init import BaseSchema, fields

class SportDTO(BaseSchema):
    sport_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)

class SportWithAthletesDTO(SportDTO):
    athletes = fields.List(fields.Nested('AthleteDTO', exclude=('sport_id',)), dump_only=True)