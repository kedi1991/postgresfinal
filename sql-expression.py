from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# exceuting from the local db
db = create_engine("postgresql:///chinook")

meta = MetaData("db")

# create  variable for the Artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)


# make the conenction
with db.connect() as connection:
    select_query = artist_table.select()
    results = connection.execute(select_query)
    for result in results:
        print(results)
