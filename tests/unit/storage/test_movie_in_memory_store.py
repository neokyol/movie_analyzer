from movie_analyzer.domain.movie import Movie
from movie_analyzer.storage.movie_in_memory_store import MovieInMemoryStore

class TestMovieInMemoryStore:
    
    def test_filter(self):
        store = MovieInMemoryStore()

        store.save_movies([
            Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)
        ])

        filtered_movies = store.filter_movies({})

        assert len(filtered_movies) == 3

        filtered_movies = store.filter_movies({'certified_fresh': False})

        assert filtered_movies == [
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)    
        ]

    def test_finder(self):
        store = MovieInMemoryStore()

        store.save_movies([
            Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)
        ])

        filtered_movies = store.find_movies(filter={}, sort_key="rating", reverse_order=True)

        assert filtered_movies == [
            Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False),   
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
        ]

        filtered_movies = store.find_movies(filter={'certified_fresh': False}, sort_key="id", reverse_order=False)

        assert filtered_movies == [
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)    
        ]

        filtered_movies = store.find_movies(filter={"rating": lambda r: r >= 7}, sort_key="id", reverse_order=False) # type: ignore

        assert filtered_movies == [
            Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)    
        ]

        filtered_movies = store.find_movies(filter={"rating": lambda r: r >= 1.9, "certified_fresh": False}, sort_key="id", reverse_order=False) # type: ignore

        assert filtered_movies == [
            Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False),
            Movie(id=3, rating=9.8, title="Blade Crawler", certified_fresh=False)    
        ]
