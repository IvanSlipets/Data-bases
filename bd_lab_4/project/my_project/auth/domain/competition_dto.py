from project.my_project.utils.db_init import BaseSchema, fields

# Схема для стикувальної таблиці
class CompetitionParticipationDTO(BaseSchema):
    participation_id = fields.Int(dump_only=True)
    athlete_id = fields.Int(required=True)
    competition_id = fields.Int(required=True)
    role = fields.Str(required=True)
    result = fields.Str(required=True)


class CompetitionDTO(BaseSchema):
    competition_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    sport_id = fields.Int(required=True)

class CompetitionWithParticipantsDTO(CompetitionDTO):
    participants = fields.List(fields.Nested('CompetitionParticipationAthleteDTO', dump_only=True))

class CompetitionParticipationAthleteDTO(CompetitionParticipationDTO):
    athlete = fields.Nested('AthleteDTO', dump_only=True)