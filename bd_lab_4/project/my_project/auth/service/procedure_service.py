from sqlalchemy import text
from project.my_project.utils.db_init import db

class ProcedureService:

    def insert_nonames(self, table, prefix, start):
        """Виклик процедури sp_insert_nonames"""
        with db.engine.connect() as conn:
            conn.execute(
                text("CALL sp_insert_nonames(:tbl, :pre, :start_val, @out_msg)"),
                {"tbl": table, "pre": prefix, "start_val": start}
            )
            res = conn.execute(text("SELECT @out_msg as msg")).fetchone()
            conn.commit() 
            
            return res[0] if res else 'OK'
            
    def link_athlete_supplement(self, first_name, last_name, supplement_name):
        """Виклик процедури для зв'язку спортсмена та добавки"""
        with db.engine.connect() as conn:
            conn.execute(
                text("CALL sp_link_athlete_supplement(:fn, :ln, :sn, @out)"),
                {"fn": first_name, "ln": last_name, "sn": supplement_name}
            )
            r = conn.execute(text("SELECT @out as msg")).fetchone()

            conn.commit()
            
            return r[0] if r else 'No result'

    def param_insert(self, table, columns, values):
        """Виклик параметризованої вставки"""
        with db.engine.connect() as conn:
            conn.execute(
                text("CALL sp_param_insert(:tbl, :cols, :vals, @out_msg);"),
                {"tbl": table, "cols": columns, "vals": values}
            )
            
            r = conn.execute(text("SELECT @out_msg as msg")).fetchone()
            
            conn.commit()
            
            return r[0] if r else 'Inserted'

    def sp_call_aggregate(self, table, column, agg):
        """Виконання агрегатної операції MAX, MIN, SUM або AVG над колонкою"""
        with db.engine.connect() as conn:
            conn.execute(
                text("CALL sp_call_aggregate(:tbl, :col, :agg_op, @res);"),
                {"tbl": table, "col": column, "agg_op": agg}
            )
            
            r = conn.execute(text("SELECT @res as value")).fetchone()
            
            return float(r[0]) if r and r[0] is not None else None

    def split_meals_to_two(self):
        """Виклик процедури для динамічного розподілу рядків у дві таблиці"""
        with db.engine.connect() as conn:
            conn.execute(text("CALL sp_split_meals_to_two();"))
            
            conn.commit()
            
            return 'Done'