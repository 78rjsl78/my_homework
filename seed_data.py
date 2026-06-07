from database import SessionLocal, User, DailyRecord
from datetime import date

db = SessionLocal()

user = db.query(User).filter(User.username == "default").first()
if user:
    user.gender = "여성"
    user.height = 165.0
    user.weight = 54.0
    db.commit()

records_data = [
    ("2026-02-28", 62.0, 10, 1.0),
    ("2026-03-31", 60.0, 20, 1.2),
    ("2026-04-30", 56.0, 30, 1.5),
    ("2026-05-31", 55.0, 40, 2.0),
    ("2026-06-04", 54.0, 45, 2.5),
]

for d, w, ext, h2o in records_data:
    r = db.query(DailyRecord).filter(DailyRecord.user_id == user.id, DailyRecord.date == d).first()
    if r:
        r.weight = w
        r.exercise_time = ext
        r.water = h2o
    else:
        r = DailyRecord(user_id=user.id, date=d, weight=w, exercise_time=ext, water=h2o, breakfast="사과 1개", lunch="닭가슴살 샐러드", dinner="고구마 1개")
        db.add(r)

db.commit()
db.close()
print("Seeding complete.")
