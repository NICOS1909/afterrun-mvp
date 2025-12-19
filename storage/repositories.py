from .db import get_conn


class ActivityRepository:
    def __init__(self):
        self.conn = get_conn()

    def initialize(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY)")
        self.conn.commit()
