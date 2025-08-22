from movie_analyzer.services.ingestion_service import CSVIngestionService
from movie_analyzer.domain.movie import Movie
from unittest.mock import Mock, mock_open, patch

class TestCSVIngestionService:
    def test_happy_path(self):
        mock_store = Mock()
        csv_content = "1,9.9,Blade Runner,True\n2,1.9,Blade Walker,False\n"

        # Mock the `open` function to return our controlled CSV content
        with patch('builtins.open', mock_open(read_data=csv_content)) as mock_file:
            service = CSVIngestionService(movie_store=mock_store, file="dummy_path.csv")
            service.ingest_movies()
            
            # Assertions
            args = mock_store.save_movies.call_args.args
            assert args[0] == [Movie(id=1, rating=9.9, title="Blade Runner", certified_fresh=True),
                               Movie(id=2, rating=1.9, title="Blade Walker", certified_fresh=False)]
            mock_file.assert_called_with("dummy_path.csv", mode='r', encoding='utf-8')

