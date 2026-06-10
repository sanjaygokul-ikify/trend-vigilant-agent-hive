from packages.core import Event, ThreatFeed, RuntimeEngine, EventStreamProcessor, MLAnomalyDetector, ContainmentEngine, PolicyEnforcement
from packages.services import Orchestrator
import unittest

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        # create pipeline components
        threat_feeds = [ThreatFeed(1, 'name', ['rule'])]
        engine = RuntimeEngine(threat_feeds)
        stream_processor = EventStreamProcessor(engine)
        anomaly_detector = MLAnomalyDetector('model_path')
        containment_engine = ContainmentEngine(PolicyEnforcement())
        orchestrator = Orchestrator(engine, stream_processor, anomaly_detector, containment_engine, PolicyEnforcement())
        # run pipeline
        orchestrator.run()

if __name__ == '__main__':
    unittest.main()