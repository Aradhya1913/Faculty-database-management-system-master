import sqlite3
import os

def connect():
    ''' Create a database if not existed and make a connection to it. '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    # Table for Students
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id INTEGER PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")

    # Table for Admin Credentials
    cur.execute("CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    cur.execute("INSERT OR IGNORE INTO admin (id, username, password) VALUES (1, 'admin', 'admin')")

    conn.commit()
    conn.close()

def verify_admin(username, password):
    ''' Verify admin credentials for login. '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result is not None

# Other Student Functions (no changes here)
def insert(fn, ln, term, gpa):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data1 VALUES (NULL,?,?,?,?)", (fn, ln, term, gpa))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn="", ln="", term="", gpa=""):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data1 WHERE fn=? OR ln=? OR term=? OR gpa=?", (fn, ln, term, gpa))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data1 WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, fn, ln, term, gpa):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE data1 SET fn=?, ln=?, term=?, gpa=? WHERE id=?", (fn, ln, term, gpa, id))
    conn.commit()
    conn.close()

def delete_data():
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()

# Call to create tables on script load
connect()