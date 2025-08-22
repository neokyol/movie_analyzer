import csv
import logging

from abc import ABC, abstractmethod
from typing import Any

from movie_analyzer.storage.movie_store import MovieStore
from movie_analyzer.domain.movie import Movie

class IngestionService(ABC):
    logger = logging.getLogger('IngestionService')

    def __init__(self, movie_store: MovieStore):
        self.movie_store = movie_store
        self.movie_list = []

    @abstractmethod
    def fetch_movies(self) -> list[Movie]:
        pass

    def ingest_movies(self):
        """Runs the service."""
        self.logger.info("Ingestion started.")
        movies: list[Movie] = self.fetch_movies()

        self.movie_store.save_movies(movies)
        self.logger.info("Ingestion ended. Processed movies = %d.", len(movies))

class CSVIngestionService(IngestionService):
    """IngestionService implementation to load movies from a CSV file and save them in the provided store.

    Attributes:
        file: filename with full path to the CSV file.
        movie_store: the store to save the data to.
    """
    def __init__(self, movie_store: MovieStore, file: str):
        super().__init__(movie_store)
        self.file = file

    def fetch_movies(self) -> list[Movie]:
        movie_list: list[Movie] = []
        with open(self.file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                movie_row = self.parse_movie(row)
                movie_list.append(movie_row)
        return movie_list      

    def parse_movie(self,  movie: Any) -> Movie:
        return Movie.from_list(movie)