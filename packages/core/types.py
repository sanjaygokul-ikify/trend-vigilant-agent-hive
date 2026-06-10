from typing import List
from dataclasses import dataclass

@dataclass
class Event:
    id: int
    type: str
    data: str

@dataclass
class ThreatFeed:
    id: int
    name: str
    rules: List[str]

    def matches(self, event: Event) -> bool:
        # Check if event matches threat feed rules
        return False
