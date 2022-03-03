import psycopg2
from config import config

def select_all(cursor):
    SQL = 'SELECT * FROM person limit 10'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def select_column_names(cursor):
    SQL = 'SELECT * FROM person WHERE false'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    
def select_certificate_data(cursor):
    SQL = 'SELECT * FROM certificates'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def select_certificate_owners(cursor):
    SQL = "SELECT person.name FROM person, certificates WHERE certificates.name = 'AZ-104' AND person.id = certificates.person_id"
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def count_rows_person(cursor):
    SQL = "SELECT COUNT(*) FROM person"
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def insert_into_certificates(cursor, cert_name, person_id):

    SQL = "INSERT INTO certificates (name,person_id) VALUES ('{}',{})".format(cert_name,person_id)
    cursor.execute(SQL)

def insert_into_person(cursor, nimi, ika, student):

    # SQL = "INSERT INTO person (name, age, student) VALUES (%s,%s,%s);"
    SQL = """INSERT INTO person (name, age, student) VALUES (%s,%s,%s);"""
    data = (nimi,ika,student)
    # SQL = "INSERT INTO person (name, age, student) VALUES ('{}',{},{})".format(nimi, ika, student)
    cursor.execute(SQL,data)

def delete_from_person(cursor, id):
    SQL = "DELETE FROM person WHERE id = (%s);"
    data = (id,)
    cursor.execute(SQL,data)
    print("deleted person id: {}".format(id))

def delete_from_certificates(cursor, id):
    SQL = "DELETE FROM certificates WHERE id = (%s);"
    data = (id,)
    cursor.execute(SQL,data)
    print("deleted certificate id: {}".format(id))

def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        
        cursor = con.cursor()
        #select_all(cursor)
        # select_column_names(cursor)
        # select_certificate_data(cursor)
        # select_certificate_owners(cursor)
        # count_rows_person(cursor)
        # insert_into_certificates(cursor, "AZ-104", "15")
        # insert_into_person(cursor, "matti", "99", "True")
        delete_from_person(cursor, "15")
        # delete_from_certificates(cursor, "15")
        con.commit()
        cursor.close()
        con.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    connect()
    