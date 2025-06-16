import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='dada0605',
    db='pet_hotel',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS owners (
        owner_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(20),
        email VARCHAR(100)
        )
        """
)

cursor.execute (
    """
    CREATE TABLE IF NOT EXISTS pets (
        pet_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        species VARCHAR(50),
        age INT,
        owner_id INT,
        FOREIGN KEY (owner_id) REFERENCES owners(owner_id)
        )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INT AUTO_INCREMENT PRIMARY KEY,
        room_type VARCHAR(50),
        price_per_day INT,
        available BOOLEAN
    )
    """
)



cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reservations (
        reservation_id INT AUTO_INCREMENT PRIMARY KEY,
        pet_id INT,
        room_id INT,
        check_in DATE,
        check_out DATE,
        FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
        FOREIGN KEY (room_id) REFERENCES rooms(room_id)
    )
    """
)

cursor.execute("INSERT INTO rooms (room_type, price_per_day, available)VALUES('Small', 50000, TRUE)")
cursor.execute("INSERT INTO rooms (room_type, price_per_day, available)VALUES('Medium', 770000, TRUE)")
cursor.execute("INSERT INTO rooms (room_type, price_per_day, available)VALUES('Large', 90000, TRUE)")

cursor.execute("CREATE TABLE IF NOT EXISTS services (service_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price INT)")
cursor.execute("INSERT INTO services (name, price) VALUES ('목욕', 15000)")
cursor.execute("INSERT INTO services (name, price) VALUES ('미용', 20000)")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reservation_services (
        reservation_id INT,
        service_id INT,
        FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
        FOREIGN KEY (service_id) REFERENCES services(service_id)
        )
    """
)

conn.commit()