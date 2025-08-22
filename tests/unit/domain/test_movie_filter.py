import pytest

from movie_analyzer.domain.movie import Movie
from movie_analyzer.domain.movie_filter import MovieFilter

class TestMovieFilter:
    movie = Movie(id=1, rating=8.8, title="Children Of Men", certified_fresh=True)

    def test_ok(self):
        filter = MovieFilter.of({"rating": lambda r: r >= 1.9} ) # type: ignore
        assert filter.isOK(self.movie) == True

        filter = MovieFilter.of({"rating": lambda r: r < 1.9} ) # type: ignore
        assert filter.isOK(self.movie) == False

        filter = MovieFilter.of({"certified_fresh": "hello"})
        assert filter.isOK(self.movie) == False

        filter = MovieFilter.of({"certified_fresh": 1})
        assert filter.isOK(self.movie) == True

    def test_unsupported_type(self):
        with pytest.raises(TypeError):
            MovieFilter.of({"some_dict": {"one": 1}})
