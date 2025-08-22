from dataclasses import dataclass
from typing import Any

@dataclass
class Movie:
    id: int
    rating: float
    title: str
    certified_fresh: bool
       
    @staticmethod
    def from_list(movie_as_list: list[Any]):
        try:
            return Movie(
                id=int(movie_as_list[0]),
                rating=float(movie_as_list[1]),
                title=str(movie_as_list[2]),
                certified_fresh=movie_as_list[3] == "True"
                )
        except ValueError:
            raise TypeError(f"Error parsing {movie_as_list}.")