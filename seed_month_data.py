from database import SessionLocal, User, DailyRecord
from datetime import date, timedelta
import random

db = SessionLocal()
user = db.query(User).filter(User.username == "default").first()

if user:
    today = date.today()
    start_date = today - timedelta(days=30)
    
    meals_b = ["사과 1개", "바나나 1개, 우유 1잔", "고구마 1개", "닭가슴살 샐러드", "오트밀", "결명자차, 식빵 1조각"]
    meals_l = ["일반식(밥 1/2 공기)", "닭가슴살 볶음밥", "연어 포케", "샌드위치 1/2", "소고기 샐러드", "현미밥과 닭가슴살"]
    meals_d = ["닭가슴살 소시지", "단백질 쉐이크", "삶은 계란 2개, 두유", "연두부 샐러드", "그릭 요거트", "토마토 샐러드"]
    
    current_weight = 56.5
    
    for i in range(30):
        d = start_date + timedelta(days=i)
        d_str = d.isoformat()
        
        # 오늘 기록은 건드리지 않음
        if d == today:
            continue
            
        r = db.query(DailyRecord).filter(DailyRecord.user_id == user.id, DailyRecord.date == d_str).first()
        
        current_weight -= random.uniform(-0.1, 0.2)
        
        ext = random.choice([0, 20, 30, 40, 50, 60])
        h2o = round(random.uniform(1.2, 2.5), 1)
        
        if r:
            r.weight = round(current_weight, 1)
            r.exercise_time = ext
            r.water = h2o
            r.breakfast = random.choice(meals_b)
            r.lunch = random.choice(meals_l)
            r.dinner = random.choice(meals_d)
        else:
            r = DailyRecord(
                user_id=user.id, 
                date=d_str, 
                weight=round(current_weight, 1), 
                exercise_time=ext, 
                water=h2o, 
                breakfast=random.choice(meals_b), 
                lunch=random.choice(meals_l), 
                dinner=random.choice(meals_d)
            )
            db.add(r)

    db.commit()

db.close()
print("Month data seeded.")
