from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine("sqlite:///mymusic.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# res = session.query(Artist).filter(Artist.name=="Kutless").first()
# print(res.name)

# res.name = "Beach Boys"
# session.commit()

artist, album = (
    session.query(Artist, Album)
    .filter(Artist.id == Album.artist_id)
    .filter(Album.title == "Thrive")
    .first()
)

album.title = "Step Up to the Microphone"
session.commit()
