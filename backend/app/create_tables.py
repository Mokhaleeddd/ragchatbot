from sqlalchemy import create_engine
from models import Base

# Replace username, password with your actual credentials
DATABASE_URL = "postgresql+psycopg2://postgres:12345678@localhost:5432/chatbot_db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print("All tables created successfully.")
