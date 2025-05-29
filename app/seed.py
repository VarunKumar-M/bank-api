from .database import SessionLocal, engine
from .models import Bank, Branch
from .database import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Open DB session
db = SessionLocal()

# Sample Banks and Branches
hdfc = Bank(name="HDFC Bank")
sbi = Bank(name="State Bank of India")

hdfc_branch = Branch(
    ifsc="HDFC0001234",
    branch="MG Road",
    address="123 MG Road",
    city="Bangalore",
    district="Bangalore Urban",
    state="Karnataka",
    bank=hdfc
)

sbi_branch = Branch(
    ifsc="SBIN0005678",
    branch="Indiranagar",
    address="456 Indiranagar",
    city="Bangalore",
    district="Bangalore Urban",
    state="Karnataka",
    bank=sbi
)

# Add to session
db.add_all([hdfc, sbi, hdfc_branch, sbi_branch])
db.commit()

print("✅ Sample data added.")

db.close()