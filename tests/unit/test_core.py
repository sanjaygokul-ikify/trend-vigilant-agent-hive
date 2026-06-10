from packages.core import Event, ThreatFeed, RuntimeEngine, EventStreamProcessor, MLAnomalyDetector, ContainmentEngine, PolicyEnforcement
import unittest

class TestCore(unittest.TestCase):
    def test_event(self):
        event = Event(1, 'type', 'data')
        self.assertEqual(event.id, 1)
        self.assertEqual(event.type, 'type')
        self.assertEqual(event.data, 'data')

    def test_threat_feed(self):
        threat_feed = ThreatFeed(1, 'name', ['rule'])
        self.assertEqual(threat_feed.id, 1)
        self.assertEqual(threat_feed.name, 'name')
        self.assertEqual(threat_feed.rules, ['rule'])

    def test_runtime_engine(self):
        engine = RuntimeEngine([])
        self.assertEqual(engine.threat_feeds, [])

    def test_event_stream_processor(self):
        engine = RuntimeEngine([])
        stream_processor = EventStreamProcessor(engine)
        self.assertEqual(stream_processor.engine, engine)

    def test_ml_anomaly_detector(self):
        detector = MLAnomalyDetector('model_path')
        self.assertEqual(detector.model_path, 'model_path')

    def test_containment_engine(self):
        containment_engine = ContainmentEngine(PolicyEnforcement())
        self.assertEqual(containment_engine.policy_enforcement, PolicyEnforcement())

if __name__ == '__main__':
    unittest.main()