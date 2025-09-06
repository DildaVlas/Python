import sqlite3
from pathlib import Path

DB_PATH = Path("db/fitness.db")

def main():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        print("=== СТАТИСТИКА ФИТНЕС-КЛУБА ===\n")

        # Статистика 1: Общее количество клиентов и их распределение по абонементам
        print("1. Клиенты по типам абонементов:")
        cur.execute("""
        SELECT 
            sp.name as plan_name,
            COUNT(c.id) as clients_count,
            sp.price as price
        FROM subscription_plans sp
        LEFT JOIN clients c ON sp.id = c.subscription_id
        GROUP BY sp.id, sp.name, sp.price
        ORDER BY clients_count DESC
        """)
        
        for row in cur.fetchall():
            print(f"  {row[0]}: {row[1]} клиентов (цена: {row[2]} руб.)")

        # Статистика 2: Загруженность тренеров
        print("\n2. Загруженность тренеров:")
        cur.execute("""
        SELECT 
            t.first_name || ' ' || t.last_name as trainer_name,
            COUNT(c.id) as clients_count,
            t.age as age
        FROM trainers t
        LEFT JOIN clients c ON t.id = c.trainer_id
        GROUP BY t.id, trainer_name, t.age
        ORDER BY clients_count DESC
        """)
        
        for row in cur.fetchall():
            print(f"  {row[0]} ({row[2]} лет): {row[1]} клиентов")

        # Статистика 3: Активность посещений
        print("\n3. Топ активных клиентов по посещениям:")
        cur.execute("""
        SELECT 
            c.first_name || ' ' || c.last_name as client_name,
            COUNT(v.id) as visits_count,
            c.phone as phone
        FROM clients c
        LEFT JOIN visits v ON c.id = v.client_id
        GROUP BY c.id, client_name, c.phone
        ORDER BY visits_count DESC
        LIMIT 5
        """)
        
        for row in cur.fetchall():
            print(f"  {row[0]} ({row[2]}): {row[1]} посещений")

        # Бонусная статистика: Общие цифры
        print("\n4. Общая информация:")
        
        cur.execute("SELECT COUNT(*) FROM clients")
        total_clients = cur.fetchone()[0]
        print(f"  Всего клиентов: {total_clients}")
        
        cur.execute("SELECT COUNT(*) FROM trainers")
        total_trainers = cur.fetchone()[0]
        print(f"  Всего тренеров: {total_trainers}")
        
        cur.execute("SELECT COUNT(*) FROM visits")
        total_visits = cur.fetchone()[0]
        print(f"  Всего посещений: {total_visits}")
        
        cur.execute("SELECT SUM(sp.price) FROM clients c JOIN subscription_plans sp ON c.subscription_id = sp.id")
        total_revenue = cur.fetchone()[0] or 0
        print(f"  Общая выручка: {total_revenue} руб.")

if __name__ == "__main__":
    main()
