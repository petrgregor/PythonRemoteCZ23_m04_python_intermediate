"""
TODO: media database

- abstraktní třída Media
  - title
  - title_cz
  - released (year)
  - description
  - genres
  - length (min)
  - rating (0-100): float
- z Media dědíme:
  - podtřídu Movie
    - directors
    - actors
  - podtřída Audio
    - author
    - narrators

- třída Human
  - name
  - surname
  - date_of_birth

  - age: metoda, která počítá věk z data narození

"""
from abc import ABC


class Media(ABC):
    """ abstraktní třída Media
      - title
      - title_cz
      - released (year)
      - description
      - genres
      - length (min)
      - rating (0-100): float
    """

    def __init__(self, title="", title_cz="", released=None, description="", genres=None, length=0, rating=0.0):
        self.title = title
        self.title_cz = title_cz
        self.released = released
        self.description = description
        self.genres = genres
        self.length = length
        self.rating = rating

    def __repr__(self):
        return (f"Media(title={self.title}, "
                f"title_cz={self.title_cz},"
                f"released={self.released},"
                f"description={self.description},"
                f"genres={self.genres},"
                f"length={self.length},"
                f"rating={self.rating})")


class Movie(Media):
    """podtřídu Movie
    - directors
    - actors
    """

    def __init__(self, title="", title_cz="", released=None, description="", genres=None, length=0, rating=0.0,
                 directors=None, actors=None):
        super().__init__(title, title_cz, released, description, genres, length, rating)
        self.directors = directors
        self.actors = actors

