import sqlite3
from pathlib import Path

DB_PATH = Path("db/fitness.db")

def main():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Тренера
        trainers_data = [
            ("Иван", "Петров", 28, "Специалист по кроссфиту и функциональным тренировкам"),
            ("Анна", "Сидорова", 25, "Персональный тренер по фитнесу и аэробике"),
            ("Михаил", "Козлов", 32, "Тренер по силовым видам спорта"),
        ]
        
        cur.executemany("""
        INSERT OR IGNORE INTO trainers (first_name, last_name, age, bio) 
        VALUES (?, ?, ?, ?)
        """, trainers_data)

        # абонементы
        plans_data = [
            ("База 1 месяц", 30, 2990.0),
            ("Стандарт 3 месяца", 90, 7990.0),
            ("Премиум 6 месяцев", 180, 14990.0),
        ]
        
        cur.executemany("""
        INSERT OR IGNORE INTO subscription_plans (name, duration_days, price) 
        VALUES (?, ?, ?)
        """, plans_data)

        # Пара клиентов
        clients_data = [
            ("Алексей", "Иванов", "+7-900-111-22-33", 1, 1),
            ("Мария", "Петрова", "+7-900-222-33-44", 2, 2),
            ("Дмитрий", "Сидоров", "+7-900-333-44-55", 1, 3),
            ("Елена", "Козлова", "+7-900-444-55-66", 3, 1),
        ]
        
        cur.executemany("""
        INSERT OR IGNORE INTO clients (first_name, last_name, phone, subscription_id, trainer_id) 
        VALUES (?, ?, ?, ?, ?)
        """, clients_data)

        #посещения (чисто для примера)
        visits_data = [
            (1, "2025-09-01 10:00:00"),
            (1, "2025-09-03 11:00:00"), 
            (2, "2025-09-02 09:30:00"),
            (3, "2025-09-01 14:00:00"),
            (4, "2025-09-04 16:30:00"),
        ]
        
        cur.executemany("""
        INSERT OR IGNORE INTO visits (client_id, visited_at) 
        VALUES (?, ?)
        """, visits_data)

        # Тестовый пользователь
        cur.execute("""
        INSERT OR IGNORE INTO users (username, password_hash) 
        VALUES ('admin', 'test_hash_123')
        """)

        conn.commit()
        print("Данные успешно добавлены в базу!")

if __name__ == "__main__":
    main()
