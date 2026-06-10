from packages.core import RuntimeEngine, EventStreamProcessor, MLAnomalyDetector, ContainmentEngine, PolicyEnforcement
from packages.utils import logging

logger = logging.get_logger(__name__)

class Orchestrator:
    def __init__(self, engine: RuntimeEngine, stream_processor: EventStreamProcessor, anomaly_detector: MLAnomalyDetector, containment_engine: ContainmentEngine, policy_enforcement: PolicyEnforcement):
        self.engine = engine
        self.stream_processor = stream_processor
        self.anomaly_detector = anomaly_detector
        self.containment_engine = containment_engine
        self.policy_enforcement = policy_enforcement

    def run(self):
        logger.info('Orchestrator running...')
        events = []
        # fetch events
        self.stream_processor.process(events)
        anomalies = self.anomaly_detector.detect_anomalies(events)
        for anomaly in anomalies:
            self.containment_engine.contain(anomaly)