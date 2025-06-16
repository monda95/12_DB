import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='dada0605',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers :", customers)
    print("customers :", customers['customerNumber'])
    print("customers :", customers['customerName'])
    print("customers :", customers['country'])
    cursor.close()

## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()
    name = 'damon'
    family_name = 'jung'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({1000}, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# add_customer()


## 3. UPDATE INTO
def uppdate_customer():
    cursor = connection.cursor()
    update_name = 'update_damon'
    contactLastName = 'update_kim'

    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# uppdate_customer()



## 4. DELETE FROM

def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)

    connection.commit()
    cursor.close()

delete_customer()
