from typing import Any, Dict
from movie_analyzer.domain.movie import Movie
from movie_analyzer.domain.movie_filter import MovieFilter
from movie_analyzer.storage.movie_store import MovieStore

class MovieInMemoryStore(MovieStore):
    def save_movies(self, movies: list[Movie]) -> None:
        self.movies = movies

    def filter_movies(self, filter: Dict[str, Any]) -> list[Movie]:
        result: list[Movie] = self.movies
        for attr, value in filter.items():
            if callable(value):
                result = [movie for movie in result if value(getattr(movie, attr, None))]
            else:
                result = [movie for movie in result if getattr(movie, attr, None) == value]
        return result
    
    def filter_movies_new(self, filters: list[MovieFilter]) -> list[Movie]:
        result: list[Movie] = self.movies
        for filter in filters:
            result = [movie for movie in result if filter.isOK(movie)]
        return result


    def find_movies(self, filter: Dict[str, Any], sort_key: str, reverse_order: bool=False) -> list[Movie]:
        return sorted(
           self.filter_movies(filter),
           key=lambda movie: getattr(movie, sort_key),
           reverse=reverse_order
        )
    
    def find_movies_new(self, filters: list[MovieFilter], sort_key: str, reverse_order: bool=False) -> list[Movie]:
        return sorted(
           self.filter_movies_new(filters),
           key=lambda movie: getattr(movie, sort_key),
           reverse=reverse_order
        )