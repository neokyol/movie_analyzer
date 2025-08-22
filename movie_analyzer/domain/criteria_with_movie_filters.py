from dataclasses import dataclass, field

from movie_analyzer.domain.movie_filter import MovieFilter

@dataclass
class CriteriaWithMovieFilters:
    filters: list[MovieFilter] = field(default_factory=list[MovieFilter])
    sort_key: str = "DESC"
    sort_order: str = "rating"
    max_rows: int = 10

