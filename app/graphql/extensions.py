from app.database.base import SessionLocal
from ariadne.types import Extension


class DatabaseExtension(Extension):
    def __init__(self):
        self.db = None

    def request_started(self, context):
        self.db = SessionLocal()
        context['database_session'] = self.db
        print(f'Opening database {self.db}')

    def request_finished(self, context):
        self.db.close()
        print(f'Closing database {self.db}')
