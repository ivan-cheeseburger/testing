from db_connect import connect_db
def add_employee(emp_no, first_name, last_name):
    db = connect_db()
    cursor = db.cursor()

    sql = "INSERT INTO employees (employee_no, first_name, last_name) VALUES (%s, %s, %s)"
    values = (emp_no, first_name, last_name)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()