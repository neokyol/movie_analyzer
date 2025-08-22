from abc import ABC, abstractmethod
from typing import Any, Dict
from movie_analyzer.domain.movie import Movie

class MovieStore(ABC):
    @abstractmethod
    def save_movies(self, movies: list[Movie]) -> None:
        pass

    @abstractmethod
    def find_movies(self, filter: Dict[str, Any], sort_key: str, reverse_order: bool=False) -> list[Movie]:
        pass

