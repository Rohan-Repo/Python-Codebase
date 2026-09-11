# Fetches all experts from SQLite DB

# ── Install sqlalchemy using pip ─────────────────────────────────────────────
# pip install sqlalchemy or pip3 install sqlalchemy

from sqlalchemy     import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy     import create_engine


# ── Create SQLite Engine ─────────────────────────────────────────────
engine = create_engine("sqlite:///ExpertDB.db")

# ── Expert table definition ──────────────────────────────────────────
class Base(DeclarativeBase):
    pass

class Expert(Base):
    __tablename__ = "Experts"
    expertID   = Column("expertID",   Integer, primary_key=True, autoincrement=True)
    birthDate  = Column("birthDate",  DateTime)
    expertName = Column("expertName", String(50))
    technology = Column("technology", String(50))


# ── Fetch and print ──────────────────────────────────────────────────
with Session(engine) as session:
    # Ascending
    experts = session.query(Expert).order_by(Expert.birthDate).all()
    # Descending
    # experts = session.query(Expert).order_by(Expert.birthDate.desc()).all()

print()
print(f"{'ID':<5} {'Expert Name':<20} {'Birth Date':<20} {'Technology':<30}")
print("-" * 75)

for expert in experts:
    birth_date_str = expert.birthDate.strftime("%Y-%m-%d %H:%M:%S") if expert.birthDate else "N/A"
    print(f"{expert.expertID:<5} {expert.expertName:<20} {birth_date_str:<20} {expert.technology:<30}")

print()
print("Total experts:", len(experts))