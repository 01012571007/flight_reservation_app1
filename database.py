import sqlite3

# إنشاء قاعدة البيانات والجدول
def init_db():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            flight_number TEXT,
            departure TEXT,
            destination TEXT,
            date TEXT,
            seat_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

# إضافة حجز جديد
def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

# جلب كل الحجوزات
def get_all_reservations():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

# حذف حجز
def delete_reservation(res_id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (res_id,))
    conn.commit()
    conn.close()

# تعديل حجز
def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    ''', (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()