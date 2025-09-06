#!/usr/bin/env python3

import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path

print("Content-Type: application/xml; charset=utf-8")
print("")

# Относительный путь к базе данных
DB_PATH = Path("db/fitness.db")


try:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, username, created_at FROM users")
        users = cur.fetchall()
        
        # Создаем XML с помощью ElementTree
        root = ET.Element("users")
        
        for user in users:
            user_elem = ET.SubElement(root, "user", id=str(user[0]))
            
            username_elem = ET.SubElement(user_elem, "username")
            username_elem.text = user[1]
            
            created_elem = ET.SubElement(user_elem, "created_at")
            created_elem.text = user[2]
        
        # Выводим XML
        print('<?xml version="1.0" encoding="UTF-8"?>')
        print(ET.tostring(root, encoding='unicode'))

except Exception as e:
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print(f"<error>{e}</error>")
