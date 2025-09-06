import sqlite3
from pathlib import Path

DB_PATH = Path("db/fitness.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def main():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name  TEXT NOT NULL,
            age INTEGER NOT NULL,
            bio TEXT
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS subscription_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration_days INTEGER NOT NULL,
            price REAL NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name  TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            subscription_id INTEGER,
            trainer_id INTEGER,
            FOREIGN KEY (subscription_id) REFERENCES subscription_plans(id) ON DELETE SET NULL,
            FOREIGN KEY (trainer_id) REFERENCES trainers(id) ON DELETE SET NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            visited_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
        );
        """)

        cur.execute("CREATE INDEX IF NOT EXISTS idx_clients_subscription ON clients(subscription_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_clients_trainer ON clients(trainer_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_visits_client ON visits(client_id);")

        conn.commit()

if __name__ == "__main__":
    main()
