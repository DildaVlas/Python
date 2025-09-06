#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sqlite3
from pathlib import Path

print("Content-Type: text/html; charset=utf-8")
print("")

# Относительный путь к базе данных
DB_PATH = Path("db/fitness.db")


print("""<!DOCTYPE html>
<html><head><title>Клиенты</title></head><body>
<h1>Список клиентов</h1>""")

try:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name, phone FROM clients")
        clients = cur.fetchall()
        
        if clients:
            print("<table border='1'>")
            print("<tr><th>Имя</th><th>Фамилия</th><th>Телефон</th></tr>")
            for client in clients:
                print(f"<tr><td>{client[0]}</td><td>{client[1]}</td><td>{client[2]}</td></tr>")
            print("</table>")
        else:
            print("<p>Клиенты не найдены</p>")
            
except Exception as e:
    print(f"<p>Ошибка: {e}</p>")

print("</body></html>")
