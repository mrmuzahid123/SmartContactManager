from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.models import Base


DATABASE_URL = "sqlite:///data/contacts.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def create_database():
    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()