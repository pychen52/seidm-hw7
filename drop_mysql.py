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

r_cursor = r_conn.cursor()

# create user and db, and grant privileges
r_cursor.execute("DROP USER 'demouser'@'localhost'")
r_cursor.execute("DROP DATABASE demo")
r_cursor.execute("FLUSH PRIVILEGES")
r_cursor.close()
r_conn.close()

