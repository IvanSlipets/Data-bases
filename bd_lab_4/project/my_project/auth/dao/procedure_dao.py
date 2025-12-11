from project.my_project.utils.db_init import db
from sqlalchemy import text
from sqlalchemy.orm import Session

class ProcedureDAO:

    def execute_proc_insert_athlete_note(self, athlete_id: int, note_text: str, note_date: str, notes_code: str):
        """Викликає збережену процедуру InsertAthleteNote."""
        try:
            with Session(db.engine) as session:
                session.execute(text("CALL InsertAthleteNote(:aid, :text, :date, :code)"), 
                                {"aid": athlete_id, "text": note_text, "date": note_date, "code": notes_code})
                session.commit()
            return True
        except Exception as e:
            raise e

    def execute_proc_participate_by_name(self, athlete_fname: str, athlete_lname: str, competition_name: str, role: str, result: str):
        """Викликає збережену процедуру ParticipateCompetitionByName."""
        try:
            with Session(db.engine) as session:
                session.execute(text("CALL ParticipateCompetitionByName(:fname, :lname, :cname, :role, :res)"), 
                                {"fname": athlete_fname, "lname": athlete_lname, "cname": competition_name, "role": role, "res": result})
                session.commit()
            return True
        except Exception as e:
            raise e

    def execute_proc_insert_batch_notes(self):
        """Викликає збережену процедуру InsertBatchNotes."""
        try:
            with Session(db.engine) as session:
                session.execute(text("CALL InsertBatchNotes()"))
                session.commit()
            return True
        except Exception as e:
            raise e

    def execute_proc_call_notes_aggregate(self, operation: str):
        """Викликає збережену процедуру CallNotesAggregate та повертає результат."""
        try:
            with Session(db.engine) as session:
                result = session.execute(text("CALL CallNotesAggregate(:op)"), {'op': operation}).fetchone()
            return result[0] if result else None
        except Exception as e:
            raise e
            
    def execute_proc_split_notes(self):
        """Викликає процедуру SplitNotesToTimestampedTables з курсором."""
        try:
            with Session(db.engine) as session:
                # Повертає назви створених таблиць
                result = session.execute(text("CALL SplitNotesToTimestampedTables()")).fetchall()
                # Перетворюємо результат у словник для зручності
                return {row[0]: row[1] for row in result}
        except Exception as e:
            raise e