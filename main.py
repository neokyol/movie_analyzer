import sys
from movie_analyzer.domain.movie_filter import MovieFilter
from movie_analyzer.domain.criteria import Criteria
from movie_analyzer.domain.criteria_with_movie_filters import CriteriaWithMovieFilters
from movie_analyzer.storage.movie_in_memory_store import MovieInMemoryStore
from movie_analyzer.services.ingestion_service import CSVIngestionService
from movie_analyzer.services.suggestions_service import SuggestionsService

def main():
    print("Starting...")
    if len(sys.argv) != 2:
        print("Usage: python main.py <movies_csv_file>", file=sys.stderr)
        sys.exit(1)
    csv_file = sys.argv[1]
    
    movie_store = MovieInMemoryStore()
    ingestion_service = CSVIngestionService(movie_store, csv_file)
    suggestion_service = SuggestionsService(movie_store)

    ingestion_service.ingest_movies()

    # criteria = Criteria(
    #     filter={'certified_fresh': True},
    #     sort_key='rating',
    #     sort_order= 'DESC',
    #     max_rows= 10
    # )
    criteria = CriteriaWithMovieFilters(
        filters=[MovieFilter.of({'certified_fresh': True})],
        sort_key='rating',
        sort_order= 'DESC',
        max_rows= 10
    )

    suggested_movies = suggestion_service.suggest_by_criteria_new(criteria)

    print("Suggested Movies:")
    for idx, movie in enumerate(suggested_movies, 1):
        print(f"{idx:02d} | {movie.title:<40} | Rating: {movie.rating:>4} | Certified Fresh: {movie.certified_fresh} | {movie.id:03d}")

if __name__ == "__main__":
    main()
