from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class Criteria:
    filter: Dict[str, Any] = field(default_factory=dict[str, Any])
    sort_key: str = "DESC"
    sort_order: str = "rating"
    max_rows: int = 10

