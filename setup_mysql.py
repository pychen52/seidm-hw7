#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
import MySQLdb.cursors

try:
    r_conn = MySQLdb.connect(host='127.0.0.1',
                            user='root',
                            passwd='root1234',
                            charset='utf8')
except:
    print("Can't Connect Database via root: ", sys.exc_info()[0])
    sys.exit()

# drop db and user if exist
r_cursor = r_conn.cursor()

# create user and db, and grant privileges
r_cursor.execute("CREATE USER 'demouser'@'localhost' IDENTIFIED BY 'demo1234'")
r_cursor.execute("CREATE DATABASE demo CHARACTER SET UTF8")
r_cursor.execute("GRANT ALL PRIVILEGES ON demo.* to 'demouser'@'localhost'")
r_cursor.execute("FLUSH PRIVILEGES")
r_cursor.close()
r_conn.close()

# connect demo db
try:
    conn = MySQLdb.connect(host='127.0.0.1',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()

# create schema
cursor = conn.cursor()
# cursor.execute("DROP TABLE if EXISTS a136")
# cursor.execute("USE demo")
cursor.execute("""CREATE TABLE rainfall (
                rpk INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name CHAR(10) NOT NULL,
                sid CHAR(5) NOT NULL,
                timestamp CHAR(25) NOT NULL,
                r_10m FLOAT(6,1) DEFAULT NULL,
                r_1h FLOAT(6,1) DEFAULT NULL,
                r_3h FLOAT(6,1) DEFAULT NULL,
                r_6h FLOAT(6,1) DEFAULT NULL,
                r_12h FLOAT(6,1) DEFAULT NULL,
                r_24h FLOAT(6,1) DEFAULT NULL,
                r_td FLOAT(6,1) DEFAULT NULL,
                r_yd FLOAT(6,1) DEFAULT NULL,
                r_2d FLOAT(6,1) DEFAULT NULL
                ) ENGINE=InnoDB""")

cursor.execute("""CREATE TABLE station (
                spk INT(5) NOT NULL PRIMARY KEY,
                name CHAR(10) NOT NULL,
                sid CHAR(5) NOT NULL,
                county CHAR(3) NOT NULL,
                lon FLOAT(7,4) NOT NULL,
                lat FLOAT(7,4) NOT NULL
                ) ENGINE=InnoDB""")

cursor.close()
conn.close()

