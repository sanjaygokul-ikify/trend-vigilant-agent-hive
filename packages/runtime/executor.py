import logging
from typing import List
from ..core.engine import RuntimeEngine
from ..core.types import Event


class Executor:
    def __init__(self, engine: RuntimeEngine):
        self.engine = engine
        self.logging = logging.getLogger(__name__)

    def execute(self, events: List[Event]):
        self.logging.info('Executing events...')
        for event in events:
            self.logging.info(f'Executing event: {event}')
            self.engine.process_events([event])

    def update_rules(self, threat_feeds: List['ThreatFeed']):
        self.engine.update_rules(threat_feeds)
        self.logging.info('Updated threat feeds...')
