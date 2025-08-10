from auth import get_password_hash
from models import User, Company, Base
from database import SessionLocal, engine

Base.metadata.create_all(engine)

db = SessionLocal()

# Insert company first
company = db.query(Company).filter(Company.company_id == "COMP123").first()
if not company:
    company = Company(company_id="COMP123", name="Test Company", hotline="123-456-7890")
    db.add(company)
    db.commit()

hashed_pw = get_password_hash("yourpassword")

new_user = User(
    name="Admin User",
    email="admin@example.com",
    password_hash=hashed_pw,
    role="admin",
    company_id="COMP123"
)

db.add(new_user)
db.commit()
db.close()

print("Admin user created successfully.")
