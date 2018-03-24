import psycopg2
from psycopg2 import sql

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = sql.SQL = (
        """
        CREATE TABLE clspeed (
            street VARCHAR(255),
            city VARCHAR(255),
            state VARCHAR(2),
            zip INTEGER,
            emm_lat decimal(12,10),
            emm_lng decimal(12,10),
            emm_acc VARCHAR(20)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server

        conn = psycopg2.connect(host="localhost",
                                database="clspeed",
                                user="clspeed",
                                password="clspeed")
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def write_entry(entry):
    commands = sql.SQL = (
        """
        INSERT INTO clspeed (street, city, state, zip, emm_lat, emm_lng, emm_acc)
        VALUES ({0},{1},{2},{3},{4},{5},{6})
        """.format(entry['street'],
                   entry['city'],
                   entry['state'],
                   entry['zip'],
                   entry['emm_lat'],
                   entry['emm_lng'],
                   entry['emm_acc']))
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server

        conn = psycopg2.connect(host="localhost",
                                database="clspeed",
                                user="clspeed",
                                password="clspeed")
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
