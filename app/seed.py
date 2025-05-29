import csv
import os
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Bank, Branch, Base

Base.metadata.create_all(bind=engine)

def seed_data():
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bank_branches.csv")
    db: Session = SessionLocal()

    banks_dict = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            bank_name = row["bank_name"]
            bank_id = int(row["bank_id"])

            # Add bank only if not already added
            if bank_id not in banks_dict:
                bank = Bank(id=bank_id, name=bank_name)
                db.add(bank)
                banks_dict[bank_id] = bank

        db.commit()

        csvfile.seek(0)
        next(reader)  # Skip header again

        for row in reader:
            branch = Branch(
                ifsc=row["ifsc"],
                bank_id=int(row["bank_id"]),
                branch=row["branch"],
                address=row["address"],
                city=row["city"],
                district=row["district"],
                state=row["state"]
            )
            db.add(branch)

        db.commit()
        db.close()
        print("✅ Data seeded successfully.")

if __name__ == "__main__":
    seed_data()
