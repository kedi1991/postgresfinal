import psycopg2

# connect to the "chinook" db
connection = psycopg2.connect(database="chinook")

# build a cursor obje for the db
cursor = connection.cursor()
# cursor.execute('SELECT * FROM "Artist"')

# select particular item
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# fetch multiple
results = cursor.fetchall()

# fetch a single
# results = cursor.fetchone()

# close the connection
connection.close()

for result in results:
    print(result)
