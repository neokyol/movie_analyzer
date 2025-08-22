from movie_analyzer.storage.movie_store import MovieStore
from movie_analyzer.domain.movie import Movie
from movie_analyzer.domain.criteria import Criteria

class SuggestionsService:
    """Service for movie suggestions

    Attributes:
        movie_store: store to retrieve movies for the suggestion.
    """
    def __init__(self, movie_store: MovieStore):
        self.movie_store = movie_store

    """Returns a list of movies according to a Criteria.

    WARNING: the current implementation of this method takes n log n time.
    It's not designed to use directly on real-time processing. A cache should be used
    or the implementation complexity should be reduced. 

    """
    def suggest_by_criteria(self, criteria: Criteria) -> list[Movie]:
        movies = self.movie_store.find_movies(criteria.filter, criteria.sort_key, reverse_order=criteria.sort_order == 'DESC')
        return movies[:criteria.max_rows]

