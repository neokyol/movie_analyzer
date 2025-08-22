import pytest

from movie_analyzer.domain.movie import Movie

class TestMovie:

    def test_happy_path(self):
        Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True)

    def test_from_list(self):
        movie_as_list = ["1", "9.9", "Blade Runner", "True"]
        movie = Movie.from_list(movie_as_list)
        
        assert movie.id == 1
        assert movie.rating == 9.9
        assert movie.title == "Blade Runner"
        assert movie.certified_fresh

    def test_from_list_alternate_rating(self):
        movie_as_list = ["1", "9", "Blade Runner", "True"]
        movie = Movie.from_list(movie_as_list)
        
        assert movie.rating == 9

    def test_from_list_numeric_title(self):
        movie_as_list = ["1", "10", "2001", "True"]
        movie = Movie.from_list(movie_as_list)
        
        assert movie.title == "2001"

    def test_invalid_id_type(self):
        with pytest.raises(TypeError):
            movie_as_list = ["AAAA", "9.9", "Blade Runner", "True"]
            Movie.from_list(movie_as_list)

    def test_invalid_rating_type(self):
        with pytest.raises(TypeError):
            movie_as_list = ["1", "9,9", "Blade Runner", "True"]
            Movie.from_list(movie_as_list)

    def test_invalid_certified_fresh_type(self):
        with pytest.raises(TypeError):
            movie_as_list = ["1", "9,9", "Blade Runner", "TRUE"]
            Movie.from_list(movie_as_list)
            
