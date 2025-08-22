from movie_analyzer.domain.criteria_with_movie_filters import CriteriaWithMovieFilters
from movie_analyzer.storage.movie_store import MovieStore
from movie_analyzer.domain.movie import Movie
from movie_analyzer.domain.criteria import Criteria

class SuggestionsService:
    def __init__(self, movie_store: MovieStore):
        self.movie_store = movie_store

    def suggest_by_criteria(self, criteria: Criteria) -> list[Movie]:
        movies = self.movie_store.find_movies(criteria.filter, criteria.sort_key, reverse_order=criteria.sort_order == 'DESC')
        return movies[:criteria.max_rows]

    def suggest_by_criteria_new(self, criteria: CriteriaWithMovieFilters) -> list[Movie]:
        movies = self.movie_store.find_movies_new(criteria.filters, criteria.sort_key, reverse_order=criteria.sort_order == 'DESC')
        return movies[:criteria.max_rows]    
        
