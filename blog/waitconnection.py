import psycopg2
import time
while True:
	try:
		conn = psycopg2.connect(dbname="blog", user="postgres", password="postgres", host="myblog-db", port="5432")
		conn.close()
		break
	except psycopg2.OperationalError:
		time.sleep(1)

print("Connection established!")