from abc import ABC, abstractmethod
from functools import singledispatch
from typing import Any, Callable, Dict
from movie_analyzer.domain.movie import Movie

class MovieFilter(ABC):
    @abstractmethod
    def isOK(self, movie: Movie) -> bool:
        pass

    def __setColumnName(self, column_name: str):
        self.column_name = column_name

    @staticmethod
    def of(arg: Dict[str, object]) -> 'MovieFilter':
        key = next(iter(arg))
        try:
            filter = MovieFilter.get(arg[key])
            filter.__setColumnName(key)
            return filter
        except TypeError:
            raise TypeError(f"Unsupported type for {arg}.")

    @singledispatch
    @staticmethod
    def get(arg: Callable[[Any], bool]) -> 'MovieFilter':
        return LambdaMovieFilter(arg)

    @get.register(str)
    @get.register(int)
    @get.register(float)
    @staticmethod
    def _(arg: str) -> 'MovieFilter':
        return EqualMovieFilter(arg)
    
    @get.register(dict)
    @staticmethod
    def _(arg: Any) -> 'MovieFilter':
        raise TypeError(f"Unsupported type {arg}.")
        

class LambdaMovieFilter(MovieFilter):
    def __init__(self, filter: Callable[[Any], bool]):
        self.filter = filter

    def isOK(self, movie: Movie) -> bool:
        return self.filter(getattr(movie, self.column_name, None))
        

class EqualMovieFilter(MovieFilter):
    def __init__(self, filter: str | int | float):
        self.filter = filter

    def isOK(self, movie: Movie) -> bool:
        return getattr(movie, self.column_name, None) == self.filter
