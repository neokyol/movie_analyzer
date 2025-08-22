from movie_analyzer.domain.criteria import Criteria
from movie_analyzer.services.suggestions_service import SuggestionsService
from movie_analyzer.domain.movie import Movie
from unittest.mock import Mock

class TestSuggestionsService:
    def test_happy_path(self):
        mock_store = Mock()
        mock_store.find_movies = Mock(return_value=[Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
                               Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False)])

        service = SuggestionsService(movie_store=mock_store)
        result = service.suggest_by_criteria(criteria=Criteria(max_rows=1))

        assert len(result) == 1


