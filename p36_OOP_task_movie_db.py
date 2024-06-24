"""
Vytvořte potřebné třídy pro práci s filmovou databází (objektově) pro:
- Genre
- Country
- People
- Movie
dle souboru 'movie.json'.

Následně ze souboru 'movie.json' načtěte všechny objekty.

Úkol 1: Vypsat seznam všech žánrů.
Úkol 2: Vypsat seznam všech zemí.
Úkol 3: Vypsat seznam všech filmů.
Úkol 4: Vypsat všechny herce.
Úkol 5: Vypsat všechny režiséry.
Úkol 6: Vypsat detail jednoho filmu (dle výběru uživatele)
Úkol 7: Vypsat detail jednoho herce (dle výběru uživatele) + seznam jeho filmů
Úkol 8: Vypočítat věk tvůrce (herce/režiséra)
Úkol 9: Vypsat filmy v pořadí od nejlešího hodnocení
Úkol 10: Vypsat seznam filmů abecedně
Úkol 11: Vypsat seznam herců abecedně (dle příjmení, jména)
"""

import json


class Genre:
    __name = None
    __pk = None

    def __init__(self, name, pk):
        self.name = name
        self.pk = pk

    def __repr__(self):
        return f"Genre: {self.name}, {self.pk}"

    def __str__(self):
        return f"Genre: {self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pk(self):
        return self.__pk

    @pk.setter
    def pk(self, pk):
        self.__pk = pk


class Country:
    __name = None
    __pk = None

    def __init__(self, name, pk):
        self.name = name
        self.pk = pk

    def __repr__(self):
        return f"Country: {self.name}, {self.pk}"

    def __str__(self):
        return f"Country: {self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pk(self):
        return self.__pk

    @pk.setter
    def pk(self, pk):
        self.__pk = pk


class People:
    __pk = None
    __name = None
    __surname = None
    __date_of_birth = None
    __date_of_death = None
    __place_of_birth = None
    __place_of_death = None
    __country = None
    __biography = None

    def __init__(self, pk=None, name=None, surname=None, date_of_birth=None, date_of_death=None,
                 place_of_birth=None, place_of_death=None, country=None, biography=None):
        self.pk = pk
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.place_of_birth = place_of_birth
        self.place_of_death = place_of_death
        self.country = country
        self.biography = biography

    def __repr__(self):
        return (f"Name: {self.name} "
                f"Surname: {self.surname}\n"
                f"Date of birth: {self.date_of_birth} "
                f"Place of birth: {self.place_of_birth}\n"
                f"Country: {self.country.name}\n"
                f"Biography: {self.biography}")

    def __str__(self):
        return f"Name: {self.name} Surname: {self.surname}"

    @property
    def pk(self):
        return self.__pk

    @pk.setter
    def pk(self, pk):
        self.__pk = pk

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def date_of_death(self):
        return self.__date_of_death

    @date_of_death.setter
    def date_of_death(self, date_of_death):
        self.__date_of_death = date_of_death

    @property
    def place_of_birth(self):
        return self.__place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        self.__place_of_birth = place_of_birth

    @property
    def place_of_death(self):
        return self.__place_of_death

    @place_of_death.setter
    def place_of_death(self, place_of_death):
        self.__place_of_death = place_of_death

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        for c in countries:
            if c.pk == country:
                self.__country = c

    @property
    def biography(self):
        return self.__biography

    @biography.setter
    def biography(self, biography):
        self.__biography = biography

    def age(self):
        pass  # TODO: vypočítat věk z data narození


class Movie:
    __pk = None
    __title_orig = None
    __title_cz = None
    __length = None
    __rating = None
    __released = None
    __description = None
    __created = None
    __countries = []
    __directors = []
    __actors = []
    __genres = []

    def __init__(self, pk=None, title_orig=None, title_cz=None, length=None, rating=None,
                 released=None, description=None, created=None,
                 countries=None, directors=None, actors=None, genres=None):

        self.pk = pk
        self.title_orig = title_orig
        self.title_cz = title_cz
        self.length = length
        self.rating = rating
        self.released = released
        self.description = description
        self.created = created
        self.countries = countries
        self.directors = directors
        self.actors = actors
        self.genres = genres

    def __repr__(self):
        return f"Title: {self.title_orig}"

    def __str__(self):
        return (f"{"-" * 35} Movie {"-" * 35}\n"
                f"Title: {self.title_orig}\n"
                f"Title czech: {self.title_cz}\n"
                f"Length: {self.length} min\n"
                f"Rating: {self.rating: .0f} %\n"
                f"Released: {self.released}\n"
                f"Description: {self.description}\n"
                f"Actors: {self.actors}\n"
                f"Directors: {self.directors}\n"
                f"Countries: {self.countries}\n"
                f"Genres: {self.genres}\n")


    @property
    def pk(self):
        return self.__pk

    @pk.setter
    def pk(self, pk):
        self.__pk = pk

    @property
    def title_orig(self):
        return self.__title_orig

    @title_orig.setter
    def title_orig(self, title_orig):
        self.__title_orig = title_orig

    @property
    def title_cz(self):
        return self.__title_cz

    @title_cz.setter
    def title_cz(self, title_cz):
        self.__title_cz = title_cz

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def released(self):
        return self.__released

    @released.setter
    def released(self, released):
        self.__released = released

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created):
        self.__created = created

    @property
    def countries(self):
        return self.__countries

    @countries.setter
    def countries(self, countries_list):
        if not self.__countries:
            self.__countries = []
        for country_pk in countries_list:
            for c in countries:
                if country_pk == c.pk:
                    self.__countries.append(c)

    @property
    def directors(self):
        return self.__directors

    @directors.setter
    def directors(self, people):
        if not self.__directors:
            self.__directors = []
        for director_pk in people:
            for p in peoples:
                if p.pk == director_pk:
                    self.__directors.append(p)

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, people):
        if not self.__actors:
            self.__actors = []
        for actor_pk in people:
            for p in peoples:
                if p.pk == actor_pk:
                    self.__actors.append(p)

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genre_list):
        if not self.__genres:
            self.__genres = []
        for genre_pk in genre_list:
            for g in genres:
                if g.pk == genre_pk:
                    self.__genres.append(g)


if __name__ == "__main__":
    genres = []
    countries = []
    peoples = []
    movies = []
    with open("movies.json", "r", encoding="UTF-8") as movies_json_file:
        movies_json = json.load(movies_json_file)
        for item in movies_json:
            print(item)
            if item["model"] == "viewer.genre":
                genre = Genre(pk=item["pk"], name=item["fields"]["name"])
                genres.append(genre)
                print(genre)
            elif item["model"] == "viewer.country":
                country = Country(pk=item["pk"], name=item["fields"]["name"])
                countries.append(country)
                print(country)
            elif item["model"] == "viewer.people":
                people = People(pk=item["pk"],
                                name=item["fields"]["name"],
                                surname=item["fields"]["surname"],
                                date_of_birth=item["fields"]["date_of_birth"],
                                date_of_death=item["fields"]["date_of_death"],
                                place_of_birth=item["fields"]["place_of_birth"],
                                place_of_death=item["fields"]["place_of_death"],
                                country=item["fields"]["country"],
                                biography=item["fields"]["biography"])

                peoples.append(people)
                print(people)
            elif item["model"] == "viewer.movie":
                movie = Movie(pk=item["pk"],
                              title_orig=item["fields"]["title_orig"],
                              title_cz=item["fields"]["title_cz"],
                              length=item["fields"]["length"],
                              rating=item["fields"]["rating"],
                              released=item["fields"]["released"],
                              description=item["fields"]["description"],
                              created=item["fields"]["created"],
                              countries=item["fields"]["countries"],
                              directors=item["fields"]["directors"],
                              actors=item["fields"]["actors"],
                              genres=item["fields"]["genres"]
                              )

                movies.append(movie)
                print(movie)

    print("Úkol 1: Vypsat seznam všech žánrů.")
    for genre in genres:
        print(genre.__repr__())

    print("\nÚkol 2: Vypsat seznam všech zemí.")
    for country in countries:
        print(country.__repr__())

    print("\nÚkol 3: Vypsat seznam všech filmů.")
    for movie in movies:
        print(movie.__repr__())

    print("\nÚkol 4: Vypsat všechny herce.")
    actors = set()
    for movie in movies:
        for actor in movie.actors:
            actors.add(actor)
    for actor in actors:
        print(actor)

    print("\nÚkol 5: Vypsat všechny režiséri.")
    directors = set()
    for movie in movies:
        for director in movie.directors:
            directors.add(director)
    for director in directors:
        print(director)

    print("\nÚkol 6: Vypsat detail jednoho filmu (dle výběru uživatele)")
    for movie in movies:
        print(f"{movie.pk}: {movie.__repr__()}")
    movie_num = int(input("\nZadejte číslo filmu: "))
    for movie in movies:
        if movie.pk == movie_num:
            print(movie)

    print("\nÚkol 7: Vypsat detail jednoho herce (dle výběru uživatele) + seznam jeho filmů")
    for actor in actors:
        print(f"{actor.pk}: {actor}")
    actor_num = int(input("\nZadejte číslo herce: "))
    for actor in actors:
        if actor.pk == actor_num:
            print(actor.__repr__())
            print("Seznam filmů, ve kterých hrál:")
            for movie in movies:
                if actor in movie.actors:
                    print(f"\t{movie.__repr__()}")
            # TODO: Seznam filmů, které režíroval ??
