import psycopg2
from config import params

def run_practice():
    conn = None
    try:
        # Подключаемся к базе
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print("--- 1. Добавляем/Обновляем пользователя (Upsert) ---")
        cur.execute("CALL upsert_user(%s, %s);", ('Mickey', '87071112233'))
        
        print("--- 2. Поиск по паттерну 'Mick' ---")
        cur.execute("SELECT * FROM get_records_by_pattern(%s);", ('Mick',))
        print("Найдено:", cur.fetchall())

        print("--- 3. Массовая вставка с валидацией ---")
        names = ['Alice', 'Bob', 'Shorty']
        phones = ['87019998877', '87025554433', '123'] # '123' слишком короткий
        cur.execute("SELECT * FROM bulk_insert_users(%s, %s);", (names, phones))
        errors = cur.fetchall()
        if errors:
            print("Ошибки валидации (не вставлены):", errors)

        print("--- 4. Пагинация (страница 1, лимит 2) ---")
        cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (2, 0))
        print("Записи:", cur.fetchall())

        print("--- 5. Удаление пользователя 'Bob' ---")
        cur.execute("CALL delete_user(%s);", ('Bob',))
        
        # Сохраняем изменения
        conn.commit()
        print("\nВсе задачи выполнены успешно!")

        cur.close()
    except Exception as e:
        print("Ошибка:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_practice()




CALL upsert_user('Arman', '87071112233');
CALL upsert_user('Madina', '87475556677');
CALL upsert_user('Karina', '87010009988');
CALL upsert_user('Batyr', '87072331456');
CALL upsert_user('Karim', '87052254923');