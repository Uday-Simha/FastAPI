from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)'''

# MYSQL Series
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
SQLALCHEMY_DATABASE_URL = "postgresql://sdgkfweg:gbrSMYK4HBTllZzb7SUwu5E67TtckBVS@pom.db.elephantsql.com/sdgkfweg"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
