from app.database.base import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DBSession:
    def __enter__(self):
        self.db = SessionLocal()
        print(f"Opening db: {self.db}")
        return self.db

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"Closing db: {self.db}")
        self.db.close()
