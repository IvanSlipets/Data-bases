from project.my_project.utils.db_init import BaseSchema, fields
from project.my_project.auth.domain.competition_dto import CompetitionParticipationDTO


class AthleteDTO(BaseSchema):
    athlete_id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    phone = fields.Str(required=True)
    email = fields.Email(required=True)
    height_cm = fields.Int(required=True)
    weight_kg = fields.Decimal(required=True)
    sport_id = fields.Int(required=True)

class AthleteWithSportDTO(AthleteDTO):
    sport = fields.Nested('SportDTO', dump_only=True)


class AthleteWithParticipationsDTO(AthleteDTO):
    participations = fields.List(fields.Nested('CompetitionParticipationCompetitionDTO', dump_only=True))

class CompetitionParticipationCompetitionDTO(CompetitionParticipationDTO):
    competition = fields.Nested('CompetitionDTO', exclude=('participants',), dump_only=True)