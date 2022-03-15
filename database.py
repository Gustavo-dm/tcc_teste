from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


engine = create_engine(
    # sqlalchemy exclusive, not needed for postgres
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Each instance of SessionLocal will be an database session, the class itself is not
# != Session from sqlAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base returns a class, this will be used to create every ORM model
Base = declarative_base()
