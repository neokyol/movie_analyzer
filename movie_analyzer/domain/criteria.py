from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class Criteria:
    """Criteria to filter and sort movies.

    Attributes:
        filter: A dictionary with movie attributes as key and value or Callable to match against.
        sort_key: the name of the movie attribute for sorting the filtering results.
        sort_order: ASC or DESC.
        max_rows: Maximum number of elements to return.
    """
    filter: Dict[str, Any] = field(default_factory=dict[str, Any])
    sort_key: str = "rating"
    sort_order: str = "DESC"
    max_rows: int = 10

